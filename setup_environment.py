#!/usr/bin/env python3
"""
Script para verificar e configurar o ambiente Appium
"""

import subprocess
import sys
import time
import requests
from pathlib import Path

def check_node_npm():
    """Verifica se Node.js e npm estão instalados"""
    try:
        node_result = subprocess.run(["node", "--version"], check=True, capture_output=True, text=True)
        npm_result = subprocess.run(["npm", "--version"], check=True, capture_output=True, text=True)
        print(f"✓ Node.js: {node_result.stdout.strip()}")
        print(f"✓ npm: {npm_result.stdout.strip()}")
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("✗ Node.js/npm não encontrado")
        print("  Instale Node.js de: https://nodejs.org/")
        return False

def check_appium():
    """Verifica se Appium está instalado"""
    try:
        result = subprocess.run(["appium", "--version"], check=True, capture_output=True, text=True)
        print(f"✓ Appium: {result.stdout.strip()}")
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("✗ Appium não encontrado")
        return False

def install_appium():
    """Instala Appium via npm"""
    print("Instalando Appium...")
    try:
        subprocess.run(["npm", "install", "-g", "appium"], check=True)
        print("✓ Appium instalado com sucesso")
        return True
    except subprocess.CalledProcessError:
        print("✗ Erro ao instalar Appium")
        return False

def check_appium_server():
    """Verifica se o servidor Appium está rodando"""
    try:
        response = requests.get("http://localhost:4723/wd/hub/status", timeout=5)
        if response.status_code == 200:
            print("✓ Servidor Appium está rodando")
            return True
    except requests.exceptions.RequestException:
        pass
    
    print("✗ Servidor Appium não está rodando")
    return False

def start_appium_server():
    """Inicia o servidor Appium em background"""
    print("Iniciando servidor Appium...")
    try:
        # Inicia Appium em background
        process = subprocess.Popen(
            ["appium"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=subprocess.CREATE_NEW_CONSOLE if sys.platform == "win32" else 0
        )
        
        # Aguarda alguns segundos para o servidor iniciar
        time.sleep(5)
        
        # Verifica se o servidor está respondendo
        if check_appium_server():
            print("✓ Servidor Appium iniciado com sucesso")
            return True
        else:
            print("✗ Erro ao iniciar servidor Appium")
            return False
            
    except Exception as e:
        print(f"✗ Erro ao iniciar Appium: {e}")
        return False

def check_adb():
    """Verifica se ADB está disponível"""
    try:
        result = subprocess.run(["adb", "version"], check=True, capture_output=True, text=True)
        print("✓ ADB está disponível")
        return True
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("✗ ADB não encontrado")
        print("  Instale Android SDK ou Android Studio")
        return False

def check_devices():
    """Verifica dispositivos conectados"""
    try:
        result = subprocess.run(["adb", "devices"], check=True, capture_output=True, text=True)
        devices = [line for line in result.stdout.split('\n') 
                  if line.strip() and 'List of devices' not in line and line.strip()]
        
        if devices:
            print("✓ Dispositivos conectados:")
            for device in devices:
                print(f"  - {device}")
            return True
        else:
            print("✗ Nenhum dispositivo conectado")
            print("  Conecte um dispositivo ou inicie um emulador")
            return False
            
    except (FileNotFoundError, subprocess.CalledProcessError):
        return False

def main():
    """Função principal"""
    print("=== Verificação do Ambiente Appium ===\n")
    
    all_good = True
    
    # Verifica Node.js e npm
    if not check_node_npm():
        all_good = False
    
    # Verifica/instala Appium
    if not check_appium():
        if check_node_npm():
            install_appium()
        else:
            all_good = False
    
    # Verifica ADB
    if not check_adb():
        all_good = False
    
    # Verifica dispositivos
    if not check_devices():
        all_good = False
    
    # Verifica/inicia servidor Appium
    if not check_appium_server():
        if check_appium():
            start_appium_server()
        else:
            all_good = False
    
    print(f"\n{'='*50}")
    if all_good:
        print("✅ Ambiente configurado e pronto para testes!")
        print("\nPara rodar os testes, use:")
        print("  python run_tests.py all")
    else:
        print("❌ Ambiente precisa de configuração")
        print("\nResolva os problemas acima e execute novamente")
    
    return 0 if all_good else 1

if __name__ == "__main__":
    sys.exit(main())
#!/usr/bin/env python3
"""
Script para executar os testes do projeto TWP Mobile com Appium
"""

import subprocess
import sys
import os
from pathlib import Path

def run_robot_tests(test_file=None, tags=None, output_dir="./logs"):
    """
    Executa os testes Robot Framework
    
    Args:
        test_file: Arquivo específico de teste (opcional)
        tags: Tags específicas para executar (opcional)
        output_dir: Diretório de saída dos logs
    """
    
    # Comando base do robot
    cmd = ["robot", "-d", output_dir]
    
    # Adiciona filtro por tags se especificado
    if tags:
        cmd.extend(["-i", tags])
    
    # Define arquivo de teste ou executa todos
    if test_file:
        cmd.append(test_file)
    else:
        cmd.append("tests/")
    
    print(f"Executando: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=False, capture_output=False)
        return result.returncode
    except FileNotFoundError:
        print("Erro: Robot Framework não encontrado. Instale com: pip install robotframework")
        return 1

def check_environment():
    """Verifica se o ambiente está configurado corretamente"""
    
    print("Verificando ambiente...")
    
    # Verifica se o Robot Framework está instalado
    try:
        result = subprocess.run(["robot", "--version"], check=False, capture_output=True, text=True)
        if result.returncode in [0, 1]:  # Robot retorna 1 mesmo quando funciona
            print("✓ Robot Framework instalado")
        else:
            print("✗ Robot Framework não encontrado")
            return False
    except FileNotFoundError:
        print("✗ Robot Framework não encontrado")
        return False
    
    # Verifica se o app existe
    app_path = Path("app/twp.apk")
    if app_path.exists():
        print("✓ App TWP encontrado")
    else:
        print("✗ App TWP não encontrado em app/twp.apk")
        return False
    
    # Verifica se o diretório de logs existe
    logs_dir = Path("logs")
    if not logs_dir.exists():
        logs_dir.mkdir()
        print("✓ Diretório de logs criado")
    else:
        print("✓ Diretório de logs existe")
    
    return True

def main():
    """Função principal"""
    
    print("=== TWP Mobile Test Runner ===\n")
    
    if not check_environment():
        print("\n❌ Ambiente não está configurado corretamente")
        return 1
    
    print("\n📱 IMPORTANTE: Certifique-se de que:")
    print("1. O servidor Appium está rodando (appium)")
    print("2. Um emulador Android está conectado ou dispositivo físico")
    print("3. O adb está funcionando (adb devices)\n")
    
    # Exemplos de execução
    print("Opções de execução:\n")
    
    print("1. Executar todos os testes:")
    print("   python run_tests.py all")
    
    print("\n2. Executar teste específico:")
    print("   python run_tests.py buttons")
    print("   python run_tests.py login")
    
    print("\n3. Executar por tags:")
    print("   python run_tests.py tag short")
    print("   python run_tests.py tag long")
    
    if len(sys.argv) < 2:
        print("\n⚠️  Nenhum argumento fornecido. Use uma das opções acima.")
        return 0
    
    command = sys.argv[1].lower()
    
    if command == "all":
        # Executa todos os testes
        return run_robot_tests()
    
    elif command == "tag" and len(sys.argv) > 2:
        # Executa testes por tag
        tag = sys.argv[2]
        return run_robot_tests(tags=tag)
    
    elif command in ["buttons", "login", "checkbox", "radio", "spinner", "swipe", "drag-and-drop", "nav", "home"]:
        # Executa teste específico
        test_file = f"tests/{command}.robot"
        return run_robot_tests(test_file=test_file)
    
    else:
        print(f"❌ Comando desconhecido: {command}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
*** Settings ***
Documentation    Aqui teremos as KWs helpers

*** Variables ***
${START}        COMEÇAR
${HAMBURGER}    xpath=//android.widget.ImageButton[@content-desc="Open navigation drawer"]

*** Keywords ***
Get Started
     Wait Until Page Contains        ${START}
     Click Text                      ${START}

Open Nav
    Wait Until Element Is Visible   ${HAMBURGER} 
    Click Element                   ${HAMBURGER} 

Go To Login Form
    Open Nav
    Click Text                  FORMS
    Wait Until Page Contains    FORMS

    Click Text                  LOGIN

Go To Radion Buttons
    Open Nav

    Click Text                  INPUTS
    Wait Until Page Contains    INPUTS
    
    Click Text                  BOTÕES DE RADIO
    Wait Until Page Contains    Escolha sua linguagem preferida

Go To Radion CheckBox
    Open Nav

    Click Text                  INPUTS
    Wait Until Page Contains    INPUTS
    
    Click Text                  CHECKBOX
    Wait Until Page Contains    Marque as techs que usam Appium

Go To Short Click
    Open Nav

    Click Text                  BOTÕES
    Wait Until Page Contains    CLIQUE SIMPLES 

    Click Text                  CLIQUE SIMPLES
    Wait Until Page Contains    Botão clique simples

 Go To long Click
    Open Nav

    Click Text                  BOTÕES
    Wait Until Page Contains    CLIQUE LONGO 

    Click Text                  CLIQUE LONGO
    Wait Until Page Contains    Botão clique longo



Go To Singup Form
    Open Nav
    Click Text                  FORMS
    Wait Until Page Contains    FORMS

    Click Text                  CADASTRO
    Wait Until Page Contains    Bem-vindo, crie sua conta.

 Go To Avenger List
    Open Nav

    Click Text                  AVENGERS
    Wait Until Page Contains    AVENGERS

    Click Text                  LISTA
    Wait Until Page Contains    LISTA    
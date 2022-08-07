*** Settings ***

Resource    ../resource/base.robot

Library    AppiumLibrary
#Executa a KW antes de cada testcase
Test Setup  Open Session
#Executa a KW depois de cada testcase
Task Teardown   Close Session


*** Variables ***
${TOOLBAR_TITLE}     	io.qaninja.android.twp:id/toolbarTitle



*** Test Cases ***
Deve acessar a tela dialogs
    Open Nav
    Click text                      DIALOGS    
    Wait Until Element Is Visible   ${TOOLBAR_TITLE} 
    Element Text Should Be          ${TOOLBAR_TITLE}     DIALOGS


Deve acessar a tela forms
    Open Nav
    Click text                      FORMS
    Wait Until Element Is Visible   ${TOOLBAR_TITLE} 
    Element Text Should Be          ${TOOLBAR_TITLE}     FORMS




Deve acessar a tela Vingadores
    Open Nav
    Click text                      AVENGERS
    Wait Until Element Is Visible   ${TOOLBAR_TITLE}
    Element Text Should Be          ${TOOLBAR_TITLE}     AVENGERS




   



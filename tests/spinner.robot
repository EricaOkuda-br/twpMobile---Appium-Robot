*** Settings ***

Resource    ../resource/base.robot

Test Setup       Open Session
Test Teardown    Close Session

*** Variables ***
${SPINNER}=    id=io.qaninja.android.twp:id/spinnerJob
${LISTOPTIONS}=    class=android.widget.ListView

*** Test Cases ***
Deve selecionar um perfil QA
    Go To Singup Form
    Choice Job    QA
    
Deve selecionar um perfil DevOps    
    Go To Singup Form
    Choice Job    DevOps


*** Keywords ***
Choice Job

    [Arguments]    ${target}

    Click Element    ${SPINNER}
    Wait Until Element Is Visible    ${LISTOPTIONS}
    Click Text    ${target}
***Settings***

Resource    ../resource/base.robot

Test Setup       Open Session
Test Teardown    Close Session

***Test Cases***
Deve clica um clique Simples
    [tags]    short
    Go To Short Click
    Click Element               id=io.qaninja.android.twp:id/short_click
    Wait Until Page Contains    Isso é um clique simples


Deve Realizar um clique looonggooo
     [tags]    long
     Go To long Click
     Long Press    id=io.qaninja.android.twp:id/long_click    1000
     Wait Until Page Contains    CLIQUE LONGO OK

# robot -d ./logs -i long tests\buttons.robot 
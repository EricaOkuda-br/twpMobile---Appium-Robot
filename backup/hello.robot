***Settings***
Library        hello.py

***Test Cases***
Deve retornar mensagem de boas vindas

        ${resultado}=      Hello Robot    EricaOK
        Should Be Equal    ${resultado}  Ola, EricaOK.  
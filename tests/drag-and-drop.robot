*** Settings ***

Resource    ../resource/base.robot

Test Setup       Open Session
Test Teardown    Close Session


*** Test Cases ***
Deve mover o Huck para o topo da lista
     Go To Avenger List

     Drang And Drop    io.qaninja.android.twp:id/drag_handle    3    0
     Sleep             3

 
*** Settings ***

Library    AppiumLibrary
Library    libs/extend.py
Resource   helpers.robot


***Keywords***
Open Session
    Set Appium Timeout  6
    Open Application    http://localhost:4723
    ...                 automationName=UiAutomator2
    ...                 platformName=Android
    ...                 deviceName=Android Device
    ...                 app=${EXECDIR}/app/twp.apk
    Get Started
Close Session
    Capture Page Screenshot
    Close Application



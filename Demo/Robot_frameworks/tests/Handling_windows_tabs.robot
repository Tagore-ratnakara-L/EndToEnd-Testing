*** Settings ***
Documentation    To validate the login form
Library    SeleniumLibrary
Library    Collections
Library    String
Test Setup        Open The Browser With Mortgage Payment Url
Test Teardown    Close Browser Session
Resource        Resource.robot
#Selenium

*** Variables ***
${login_button}        xpath://input[@id='signInBtn']
${email}                  

*** Test Cases ***
Validate Child window Functionality
    Select the link 0f Child window
    Verify the user is Switched to Child window
    Grab the Email id in the Child Window
    Switch to the Parent Window and enter the Email

*** Keywords ***
Select the link 0f Child window
    Click Element    xpath://a[@class='blinkingText']  
    Sleep    5

Verify the user is Switched to Child window
    Switch Window    NEW
    Element Text Should Be    css:h1    DOCUMENTS REQUEST

Grab the Email id in the Child Window
    ${text}=    Get Text    css:.im-para.red
    @{words}=    Split String    ${text}    at
    #at 0 index = Please email us
    #at 1 index =  mentor@rahulshettyacademy.com with below template to receive response 
    ${text_split}=    Get From List    ${words}    1
    Log    ${text_split}
    @{word_1}=    Split String    ${text_split}
    ${email}=    Get From List    ${word_1}    0
    Set Global Variable    ${email}
    
Switch to the Parent Window and enter the Email
    Switch Window    MAIN
    Title Should Be    LoginPage Practise | Rahul Shetty Academy
    Input Text    id:username    ${email}


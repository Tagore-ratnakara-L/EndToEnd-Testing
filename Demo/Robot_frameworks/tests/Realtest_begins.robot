*** Settings ***
Documentation    To validate the login form
Library    SeleniumLibrary
Test Setup        Open The Browser With Mortgage Payment Url
Test Teardown    Close Browser Session
Resource        Resource.robot
#Selenium

*** Variables ***
${Error_message_Login}    css:.alert.alert-danger.col-md-12

*** Test Cases ***
Validate UnSuccessful Login
    Fill the login Form    ${user_name}    ${invalid_password}
    wait until Element is located in the page    ${Error_message_Login}
    verify error message is correct
    
Validate Cards display in the Shopping Page
    Fill the login Form    ${user_name}    ${valid_password}
    wait until Element is located in the page    

*** Keywords ***
Fill the login Form
    [Arguments]    ${username}    ${password}
    Input Text        xpath://input[@id='username']    ${username}
    Input Password    xpath://input[@id='password']    ${password}
    Click Button      xpath://input[@id='signInBtn']

wait until it checks and display error message
    [Arguments]    ${PageElement}
    Wait Until Element Is Visible    ${PageElement}

wait until Element is located in the page  

verify error message is correct
    Element Text Should Be    ${Error_message_Login}    Incorrect username/password.
    

    
    
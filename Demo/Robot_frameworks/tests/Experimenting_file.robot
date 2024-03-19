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
    Fill the login Form
    wait until it checks and display error message
    verify error message is correct

*** Keywords ***
Fill the login Form
    Input Text        xpath://input[@id='username']    ${user_name}
    Input Password    xpath://input[@id='password']    ${invalid_password}
    Click Button      xpath://input[@id='signInBtn']

wait until it checks and display error message
    Wait Until Element Is Visible    ${Error_message_Login}

verify error message is correct
    Element Text Should Be    ${Error_message_Login}    Incorrect username/password.
    

    
    
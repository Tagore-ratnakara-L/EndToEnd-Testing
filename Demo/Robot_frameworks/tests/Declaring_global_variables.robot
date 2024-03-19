*** Settings ***
Documentation    To validate the login form
Library    SeleniumLibrary
Test Teardown    Close Browser
#Resource
#Selenium

*** Variables ***
${Error_message_Login}    css:.alert.alert-danger.col-md-12

*** Test Cases ***
Validate UnSuccessful Login
    open the browser with Mortgage payment url
    Fill the login Form
    wait until it checks and display error message
    verify error message is correct

*** Keywords ***
open the browser with Mortgage payment url
    Create Webdriver    Chrome
    Go To    https://rahulshettyacademy.com/loginpagePractise/

Fill the login Form
    Input Text        xpath://input[@id='username']    rahulshettyacademy
    Input Password    xpath://input[@id='password']    123456789
    Click Button      xpath://input[@id='signInBtn']

wait until it checks and display error message
    Wait Until Element Is Visible    ${Error_message_Login}

verify error message is correct
    Element Text Should Be    ${Error_message_Login}    Incorrect username/password.
    

    
    
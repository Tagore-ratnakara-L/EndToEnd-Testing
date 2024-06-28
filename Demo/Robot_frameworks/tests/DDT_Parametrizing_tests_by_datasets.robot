*** Settings ***
Documentation    To Validate the Login form
Library    SeleniumLibrary
Test Teardown    Close Browser
Test Template    Validate Unsuccessful Login

*** Variables ***
${Error_message_Login}    css:.alert.alert-danger.col-md-12

*** Test Cases ***    username    password
Invalid username    deafed    learning
Invalid Password    rahulshetty    pudding
Special Characters    @#!@&%    learning

    
*** Keywords ***
Validate Unsuccessful Login
    [Arguments]    ${username}    ${password}
    open the browser with Mortgage payment url
    Fill the login Form    ${username}    ${password}
    wait until it checks and display error message
    verify error message is correct


open the browser with Mortgage payment url
    Create Webdriver    Chrome
    Go To    https://rahulshettyacademy.com/loginpagePractise/

Fill the login Form
    [Arguments]    ${username}    ${password}
    Clear Element Text    xpath://input[@id='username']
    Input Text        xpath://input[@id='username']    ${username}
    Clear Element Text    xpath://input[@id='password']
    Input Password    xpath://input[@id='password']    ${password}
    Click Button      xpath://input[@id='signInBtn']

wait until it checks and display error message
    Wait Until Element Is Visible    ${Error_message_Login}

verify error message is correct
    Element Text Should Be    ${Error_message_Login}    Incorrect username/password.
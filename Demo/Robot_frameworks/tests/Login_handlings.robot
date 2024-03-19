*** Settings ***
Documentation    To validate the login form
Library    SeleniumLibrary
Library    Collections
Test Setup        Open The Browser With Mortgage Payment Url
Test Teardown    Close Browser Session
Resource        Resource.robot
#Selenium

*** Variables ***
${login_button}        xpath://input[@id='signInBtn']

*** Test Cases ***
Validate Cards display in the Shopping Page
    Fill the Login Details and select the User option

*** Keywords ***
Fill the Login Details and select the User option
    
    Input Text    xpath://input[@id='username']    rahulshettyacademy
    Input Password    xpath://input[@id='password']    learning
    Click Element    css:input[value='user']
    Wait Until Element Is Visible    css:.modal-body
    Click Element    okayBtn
    Click Element    okayBtn
    Select From List By Value    css:select.form-control    teach
    Select Checkbox    terms
    Checkbox Should Be Selected    terms
#    Click Button    ${login_button}
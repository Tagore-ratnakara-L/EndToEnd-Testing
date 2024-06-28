*** Settings ***
Documentation    All Pages need to be validated by Page objects and keywords of landing page
Library          SeleniumLibrary
Resource        Generic.robot

*** Variables ***
#${shop_page_load}        css:.nav-link.btn.btn-primary
${Error_message_Login}    css:.alert.alert-danger.col-md-12

*** Keywords ***

Fill the Login Form
    [Arguments]    ${username}    ${password}
    Input Text    username    ${username}
    Input Password    password    ${password}
    Click Button    signInBtn
    Sleep    2

wait until Element is located in the page
    wait until Element passed is located on the page    ${Error_message_Login}
    
verify error message is correct
    Element Text Should Be    ${Error_message_Login}    Incorrect username/password.
    
Fill the Login details and Login Form
    Input Text    username    rahulshettyacademy
    Input Password    password    learning
    Click Element    css:input[value='user']
    Sleep    2
    Wait Until Element Is Visible    css:.modal-body
    Click Element    okayBtn
    Sleep    2
#    Click Element    okayBtn
#    Sleep    2
    Click Element    xpath://select[@data-style='btn-info']
    Select From List By Value    css:select.form-control    teach
    Sleep    2
    Select Checkbox    terms
    Checkbox Should Be Selected    terms
#    Click Button    ${login_button}    
    
*** Settings ***
Documentation    To validate the login form
Library    SeleniumLibrary
Library    Collections
Test Setup        Open The Browser With Mortgage Payment Url
#Test Teardown    Close Browser Session
Resource        Resource.robot
#Selenium

*** Variables ***
${Error_message_Login}    css:.alert.alert-danger.col-md-12
${shop_page_load}        css:.nav-link.btn.btn-primary
${login_button}        xpath://input[@id='signInBtn']

*** Test Cases ***
#Validate UnSuccessful Login
#    Fill the login Form    ${user_name}    ${invalid_password}
#    wait until Element is located in the page    ${Error_message_Login}
#    verify error message is correct  
Validate Cards display in the Shopping Page
    Fill the login Form    ${user_name}    ${valid_password}
    wait until Element is located in the page    ${shop_page_load}
    Verify Card titles in the Shop page
    Select the Cart    Samsung Note 8
    Fill the Login Details and select the User option

*** Keywords ***
Fill the login Form
    [Arguments]    ${username}    ${password}
    Input Text        xpath://input[@id='username']    ${username}
    Input Password    xpath://input[@id='password']    ${password}
    Click Button      ${login_button}

wait until Element is located in the page
    [Arguments]    ${PageElement}
    Wait Until Element Is Visible    ${PageElement}

verify error message is correct
    Element Text Should Be    ${Error_message_Login}    Incorrect username/password.
    
Verify Card titles in the Shop page
    @{expected_list}=    Create List    iphone X    Samsung Note 8    Nokia Edge    Blackberry
    ${elements}=    Get WebElements    css:.card-title
    ${actual_list}=    Create List
    FOR    ${element}    IN    @{elements}
        Log    ${element.text}
        Append To List    ${actual_list}    ${element.text}
    END
    Lists Should Be Equal    ${expected_list}    ${actual_list}

Select the Cart
    [Arguments]    ${cartName}
    ${elements}=    Get Webelements    css:.card-title
    ${index}=    Set Variable    1
    FOR    ${element}    IN    @{elements}
        Exit For Loop If    '${cartName}' == '${element.text}'
        ${index}=    Evaluate    ${index} + 1
    END
    Click Button    xpath:(//button[@class='btn btn-info'])[${index}]

Fill the Login Details and select the User option
    
    Input Text    xpath://input[@id='username']    rahulshettyacademy
    Input Password    xpath://input[@id='password']    learning
    Click Element    css:input[value='user']
    
    
    
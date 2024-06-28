*** Settings ***
Documentation    All Pages need to be validated by Page objects and keywords of landing page
Library          SeleniumLibrary
Library    Collections
Resource    Generic.robot

*** Variables ***
${shop_page_load}    css:a.btn

*** Keywords ***

wait until Element is located in the page
    wait until Element passed is located on the page    ${shop_page_load}
    Sleep    2

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



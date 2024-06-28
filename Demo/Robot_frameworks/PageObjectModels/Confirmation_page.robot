*** Settings ***
Documentation    All Pages need to be validated by Page objects and keywords of landing page
Library          SeleniumLibrary
Library    Collections
Resource    Generic.robot

*** Variables ***
${Conf_country}    xpath://a[text()='India']

*** Keywords ***

Enter your Country and accept Terms
    [Arguments]    ${country_name}
    Sleep    2
    Click Element    xpath://input[@id='country']
    Sleep    2
    Input Text    country    ${country_name}
    Sleep    2
    wait until Element passed is located on the page    ${Conf_country}
    Sleep    2
    Click Element    ${Conf_country}
    Sleep    2
    Click Element    css:.checkbox label
    Sleep    2

Purchase and validate the success Message
    Click Button    xpath://input[@type='submit']
    Sleep    2
    Page Should Contain Element    xpath://strong[normalize-space()='Success!']
*** Settings ***
Documentation    A resource file with reusable keywords and variables.
...
...              The system specific keywords created here from our own
...              domain specific language. They utilize keyword provided
...              by the SeleniumLibrary.
Library          SeleniumLibrary

*** Variables ***
${user_name}            rahulshettyacademy
${invalid_password}        123456789
${valid_password}        learning
${url}            https://rahulshettyacademy.com/loginpagePractise/
${browser_name}    Chrome

*** Keywords ***
drive url with given customized browser  
#    [Arguments]    ${browser_name}
    Create Webdriver    ${browser_name}
    Go To        ${url}
        
    
    
open the browser with given url
    Create Webdriver    Chrome
    Go To        ${url}

wait until Element passed is located on the page
    [Arguments]    ${PageLocator}
    Wait Until Element Is Visible    ${PageLocator}

Close Browser session
    Close Browser
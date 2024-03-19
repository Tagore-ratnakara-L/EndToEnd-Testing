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



*** Keywords ***
open the browser with Mortgage payment url
    Create Webdriver    Chrome
    Go To        ${url}

Close Browser session
    Close Browser
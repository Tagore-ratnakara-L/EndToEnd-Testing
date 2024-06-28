*** Settings ***
Documentation    All Pages need to be validated by Page objects and keywords of landing page
Library          SeleniumLibrary
Library    Collections


*** Keywords ***
Verify Items in the checkout Page and Proceed
    Sleep    5
    Click Button    css:.btn-success
    Sleep    5

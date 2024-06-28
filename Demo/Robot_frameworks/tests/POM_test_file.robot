*** Settings ***
Documentation    To validate the login form

Library    SeleniumLibrary
Library    Collections
Library    ../Customized_Libraries/ShoppingCard.py

Test Setup        Generic.drive url with given customized browser
Test Teardown    Close Browser Session

Resource        ../PageObjectModels/Generic.robot
Resource        ../PageObjectModels/LandingPage.robot
Resource        ../PageObjectModels/ShopPage.robot
Resource        ../PageObjectModels/Checkout_Page.robot
Resource        ../PageObjectModels/Confirmation_page.robot


#Selenium

*** Variables ***

@{ListOfProducts}    Nokia Edge    Blackberry
${login_button}        xpath://input[@id='signInBtn']
${country_name}    India

*** Test Cases ***
Validate UnSuccessful Login
    [Tags]    SMOKE
    LandingPage.Fill the login Form    ${user_name}    ${invalid_password}
    LandingPage.wait until Element is located in the page
    LandingPage.verify error message is correct
Validate Cards display in the Shopping Page
    [Tags]    Regression
    LandingPage.Fill the login Form    ${user_name}    ${valid_password}
#    ShopPage.wait until Element is located in the page
    ShopPage.Verify Card titles in the Shop page
    add item to cart and checkout    ${ListOfProducts}
    Checkout_Page.Verify Items in the checkout Page and Proceed
    Confirmation_page.Enter your Country and accept Terms    ${country_name}
    Confirmation_page.Purchase and validate the success Message
#    Select the Cart    Samsung Note 8

Select the Form and navigate to the Child window
    [Tags]    Sanity    Acceptance
    LandingPage.Fill the Login details and Login Form





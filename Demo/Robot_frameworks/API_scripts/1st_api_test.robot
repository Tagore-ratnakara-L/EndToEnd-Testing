*** Settings ***
Library    Collections
*** Test Cases ***

Play around with dictionary
    &{data}=    Create Dictionary    name=rahulshetty    course=robot    website=rahulshettyacademy.com
    Log    ${data}
    Dictionary Should Contain Key    ${data}    name
    Log    ${data}[name]
    ${url}=    Get From Dictionary    ${data}    website
    Log    ${url}
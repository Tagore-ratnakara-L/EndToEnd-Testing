Feature: Feature: Verify login page test cases

 Scenario: Login Page validation with query params

   Given Navigate to OrangeHRM in browser
   When Validating with below params
    | userName | password |
    | Admin    | admin123 |
   Then Verify login Home status is successful or not

#     | Admin    | asdf*123 |
#     | asdf*123 | admin123 |

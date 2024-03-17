Feature: Feature: Verify login page test cases

 Scenario Outline: Login Page validation Username and Password

   Given Open OrangeHRM in browser
   When Validating <username> and <password>
   Then Verify login Home status

   Examples:
     | username | password |
     | Admin    | admin123 |
     | Admin    | asdf*123 |
     | asdf*123 | admin123 |


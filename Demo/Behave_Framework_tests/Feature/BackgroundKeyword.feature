Feature: Verify login page test cases

  Background:
    Given Open Orange_HRM browser

#  @smoke
  Scenario: Login with valid Username and Password

#    Given Open Orange_HRM browser
    When providing valid UsernamE and PassworD
    Then verifying login is successful or not

#  @regression
#  Scenario: Opening google page and verify title
#
#    Given Open Orange_HRM browser
#    When Provided google url in browser
#    Then Verify title of the google page

#  @sanity
  Scenario Outline: Login Page validation Username and Password

#    Given Open Orange_HRM browser
    When Passing the below <UserName> and <PassWord> in params
    Then Verifying login Home status
    Examples:
      | UserName | PassWord |
      | Admin    | admin123 |
      | Admin    | asdf*123 |
      | asdf*123 | admin123 |

#  @Tagore
  Scenario: Login Page validation with query params

#    Given Open Orange_HRM browser
    When Validating with below parameters
      | userName | Password |
      | Admin    | admin123 |
    Then Verifying login Home status is successful or not
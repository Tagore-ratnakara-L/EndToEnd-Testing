  # tags used to run some particular test cases in a group of test Scenarios and functions like mentioning
  # @smoke
  # sanity
  # regression
  # etc...
    # CMD  = behave folder/<file>.feature --tags=sanity  or behave folder/<file>.feature --tags="sanity"

Feature: Verify login page test cases
  @smoke
  Scenario: Login with valid Username and Password

    Given Open OrangeHRM browser
    When Provide valid username and password
    Then Verify login is successful or not

  @regression
  Scenario: Opening google page and verify title

    Given Opening browser
    When Provided google url in browser
    Then Verify title of the google page

  @sanity
  Scenario Outline: Login Page validation Username and Password
    Given Open OrangeHRM in browser
    When Validating <username> and <password>
    Then Verify login Home status

   Examples:
     | username | password |
     | Admin    | admin123 |
     | Admin    | asdf*123 |
     | asdf*123 | admin123 |

  @Tagore
  Scenario: Login Page validation with query params
    Given Navigate to OrangeHRM in browser
    When Validating with below params
     | userName | password |
     | Admin    | admin123 |
    Then Verify login Home status is successful or not
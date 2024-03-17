Feature: Verify login page test cases

  Scenario: Login with valid Username and Password

    Given Open OrangeHRM browser
    When Provide valid username and password
    Then Verify login is successful or not
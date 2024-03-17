Feature: Sample Code testing

  Scenario: Opening google page and verify title

    Given Opening browser
    When Provided google url in browser
    Then Verify title of the google page

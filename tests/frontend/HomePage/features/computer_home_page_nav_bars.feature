
@smoke2
Feature: Navigation bars in the home page

    @tcid03
    Scenario: Verify the navigation bars on home page are visible

      Given I go to the site "computer-database.gatling.io"
      Then the "main navigation" bar should be visible
      And the "top navigation" bar should be visible
      And the "options" bar should be visible
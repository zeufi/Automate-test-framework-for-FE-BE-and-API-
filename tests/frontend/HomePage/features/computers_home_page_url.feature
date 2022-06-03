
@smoke1
Feature: Verifying the home page url goes to the right place

    @tcid01
    Scenario: The Computer home page should have correct title

        Given I go to the site "computer-database.gatling.io"
        Then the page title should be "Computers database"

    @tcid02
    Scenario: The Python home page should have correct url

        Given I go to the site "computer-database.gatling.io"
        Then current url should be "https://computer-database.gatling.io/computers"
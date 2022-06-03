
  @smoke4
  Feature: Product API Smoke

    @@tcid05
    Scenario: Verify 'get all products' returns the expected number of products

        #Given I get number of available computers from db
        When I get number of available computers from api
        Then the total number of computers in api should be same as in db

    @@tcid06
    Scenario: Verify 'computers/id' returns a computer with the given id

      Given I get 1 random computer from database
      Then I verify product api returns correct computer by id
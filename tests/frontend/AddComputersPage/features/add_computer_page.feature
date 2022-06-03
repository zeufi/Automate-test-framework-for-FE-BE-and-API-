
  @smoke3
  Feature: Add computers

    @@tcid04
    Scenario: User should be able to add computer

      Given I go to the site "computer-database.gatling.io"
      When I click on the 'add new computer' button
      And I type "New Macbook" into username of computer name form
      And Then I click on the 'Create this computer' button
      Then New computer should be created


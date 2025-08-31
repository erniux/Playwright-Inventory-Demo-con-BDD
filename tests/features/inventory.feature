Feature: Inventory management
  As a QA
  I want to validate the inventory table
  So that I can ensure the system loads correctly

  Background: 
    Given I open the inventory demo

  Scenario: Open inventory page
    Then I should see the inventory table

  Scenario: Verify product exists in inventory
    When I search for product "Pet Shop Boys"
    Then I should see "Pet Shop Boys" in the results

  Scenario: Verify product does not exist in inventory
    When I search for product "Unicorn Laptop"
    Then I should see no results in the table

  Scenario: Verify multiple results appear for partial search
    When I search for product "2020"
    Then I should see multiple results in the table

  Scenario: Verify inventory table has required columns
    Then I should see the columns "Album Name, Artist, Year, Price"

  Scenario: Verify sorting by Est. Profit column ascending
    When I sort the table by "Est. Profit" ascending
    Then the values in "Est. Profit" should be sorted ascending

  Scenario: Verify sorting by Est. Profit column descending
    When I sort the table by "Est. Profit" descending
    Then the values in "Est. Profit" should be sorted descending

  #Scenario: Verify pagination updates table records
  #  When I go to the next page of the table
  #  Then I should see different results compared to the first page

  #Scenario: Verify page size change updates rows
  #  When I change the page size to "100"
  #  Then I should see more rows displayed than with the default size

    
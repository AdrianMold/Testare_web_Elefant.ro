Feature: Testing the Website www.elefant.ro


    Scenario:1.When I fill in all required fields with valid data
    Given We are on the login page
    When I have accepted cookies
    When I enter the email address "alaaabalaaa3@yahoo.com"
    When I enter password "portocala"
    When I press the login button
    Then I should be logged in with my email address

    Scenario:2.Searching for a book in the search bar
    Given We are on the main page of www.elefant.ro
    When I enter "Harry Potter" in the search bar
    When I click on the search button
    Then I should receive a list of "Harry Potter" books

    Scenario:3.Filling in with wrong email and password
     Given I am on the login page
     When I log out
     When I navigate back on the login page
     When I fill in with wrong email
     When I fill in with wrong password
     When I click the login button
     Then I should see an error message

    Scenario:4.Verifying the main page title
     Given I am on the main page of www.elefant.ro
     Then The elefant.ro logo should be present

    Scenario:5.Verifying the display of a promotional banner
     Given You are on the main page of www.elefant.ro
     When A promotional banner should be displayed
     Then Click on the promotional banner

    Scenario:6.Accessing the Delivery Location
     Given User is on the main page
     When User clicks on the "Puncte Livrare" link
     Then User should be on the Puncte Livrare page

    Scenario:7.Navigating through the menu to a specific category
     Given User1 on the main page of www.elefant.ro
     When User1 clicks the "Categorii"
     When User1 navigates through the menu to "Electronice & IT"
     Then User1 should see products related to "Electronice & IT"

    Scenario:8.Adding a product to the shopping cart
     Given User2 is on the main page of www.elefant.ro
     When User2 searches for "Joc Monopoly" in the search bar
     When User2 clicks on the search button
     When User2 reveives a list of "Monopoly" games
     When User2 selects the first product from the search results
     When User2 adds the product to the shopping cart
     Then The product should be in User2's shopping cart

     Scenario:9.Removing a product from the shopping cart
      Given User3 is on the main page of www.elefant.ro
      When User3 navigates to the shopping cart
      When User3 clicks the "Remove" button for a specific product
      Then The product should be removed from the shopping cart

     Scenario:10.Searching with Special Characters in the Search Bar
      Given User4 is on the main page of www.elefant.ro
      When User4 types special characters "§$%&/" into the search bar and presses the search button
      Then An appropriate message indicating no results should be displayed






































Feature: Searching for a contact as an admin
    As an admin
    I want to have the ability to search for a contact point
    So that I can obtain results based on the search

    Background: User logged in with Admin credentials
        Given the user is on the login page
        When the user enters valid credentials
        And the user clicks the "Log In" button

    Scenario: Search by valid contact
        Given logged in user is on the Contact Search page
        When the user enters a valid contact name "Automation Contact Point Test"
        And the user clicks the Search button
        Then the searched contact "Automation Contact Point Test" is displayed

    Scenario: Search by valid email address
        Given logged in user is on the Contact Search page
        When the user enters a valid email address "test.automations@test.com"
        And the user clicks the Search button
        Then the searched contact by the email address "test.automations@test.com" is displayed

    Scenario: Search by invalid contact
        Given logged in user is on the Contact Search page
        When the user enters an invalid contact name "hdsakjhdsak" 
        And the user clicks the Search button
        Then the message "Number of matching contacts: 0" is displayed
        And the search results table should have 0 rows
        
    Scenario: Search by an empty value
        Given logged in user is on the Contact Search page
        When the user clicks the Search button
        Then a list of results is returned

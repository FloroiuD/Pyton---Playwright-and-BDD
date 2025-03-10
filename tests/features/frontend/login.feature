Feature: Login
    As a user
    I want to be able to login 
    So that I can access my account

    Scenario: Successful Login 
        Given the user is on the login page
        When the user enters valid credentials
        And the user clicks the "Log In" button
        Then a notice message "Welcome. You have been logged in." should be displayed
        And the user should be redirected to the dashboard

    Scenario: Failed Login with invalid username and password
        Given the user is on the login page
        When the user enters invalid credentials
        And the user clicks the "Log in" button
        Then an alert message "Invalid username or password." should be displayed
        And the user should not be redirected to the dashboard

    Scenario: Failed Login with empty fields 
        Given the user is on the login page
        When the user leaves the credentials empty
        And the user clicks the "Log In" button
        Then an alert message "Invalid username or password." should be displayed 
        And the user should not be redirected to the dashboard

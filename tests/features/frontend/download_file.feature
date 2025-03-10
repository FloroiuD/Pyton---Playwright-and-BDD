Feature: Get the Test Documnet
    As an admin
    I want to download the Document 1
    So that I can verify the download functionality works as expected

    Background: Background name
        Given the user is on the login page
        When the user enters valid credentials
        And the user clicks the "Log In" button
        And the tmp folder is deleted

    Scenario: Download the Test Document
        Given the logged in user navigates to an active business organization page with the ID "1122112"
        And the user clicks on the "Documents" tab
        When the user clicks on the "Get the Document" button
        And the user initiates the download by clicking "Test Document (zip)"
        Then a zip file is downloaded

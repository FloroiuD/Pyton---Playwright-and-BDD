from playwright.sync_api import Page, expect
from pytest_bdd import given, when, then, parsers
from config import BASE_URL


@given('logged in user is on the Contact Search page')
def navigate_to_contact_search_page(page: Page):
    page.goto(f"{BASE_URL}/admin/contacts/search")


@when(parsers.parse('the user enters a valid contact name "{text}"'))
@when(parsers.parse('the user enters a valid email address "{text}"'))
@when(parsers.parse('the user enters an invalid contact name "{text}"'))
def contact_search_input_field(page: Page, text):
    page.locator("#keyword").fill(text)


@when(parsers.parse('the user clicks the Search button'))
def click_search_button(page: Page):
    page.get_by_text("Search", exact=True).click()


@then(parsers.parse('the searched contact "{text}" is displayed'))
@then(parsers.parse('the searched contact by the email address "{text}" is displayed'))
def search_results_by_name(page: Page, text):
    expect(page.locator(f"#main_content > table > tbody > tr:has-text('{text}')")).to_be_visible()


@then(parsers.parse('the message "{text}" is displayed'))
def zero_matching_contacts_message(page: Page, text):
    expect(page.locator("#main_content > div > p")).to_have_text(text)


@then('the search results table should have 0 rows')
def verify_zero_rows_in_search_results(page: Page):
    expect(page.locator("#main_content > table > tbody > tr:not(:first-child)")).to_have_count(0)


@then('a list of results is returned')
def list_of_results(page: Page):
    expect(page.locator("#main_content > table > tbody > tr:not(:first-child)")).not_to_have_count(0)

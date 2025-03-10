from pytest_bdd import given, when, then, parsers
from playwright.sync_api import Page, expect
from basic_authentication_model.basic_authentication import BasicAuthentication
from config import BASE_URL, USERNAME, PASSWORD


@given('the user is on the login page')
def visit_login_page(page: Page):
    BasicAuthentication.execute(page)
    page.goto(f"{BASE_URL}/login")


@when('the user enters valid credentials')
@given('the user enters valid credentials')
def input_valid_credentials(page: Page):
    page.get_by_label("Username").fill(USERNAME)
    page.get_by_label("Password").fill(PASSWORD)


@then(parsers.parse('a notice message "{text}" should be displayed'))
def assert_login_successful(page: Page, text):
    expect(page.locator(".flash.notice")).to_have_text(text)


@then('the user should be redirected to the dashboard')
def verify_user_redirected_to_dashboard(page: Page):
    expect(page).to_have_url(url_or_reg_exp=f"{BASE_URL}/admin/dashboard")


@when('the user enters invalid credentials')
def input_invalid_credentials(page: Page):
    page.get_by_label("Username").fill("Test")
    page.get_by_label("Password").fill("Password")


@then(parsers.parse('an alert message "{text}" should be displayed'))
def assert_login_failed(page: Page, text):
    expect(page.locator(".flash.alert")).to_have_text(text)


@then('the user should not be redirected to the dashboard')
def verify_user_not_redirected(page: Page):
    expect(page).not_to_have_url(url_or_reg_exp=f"{BASE_URL}/admin/dashboard")


@when('the user leaves the credentials empty')
def empty_credentials():
    pass

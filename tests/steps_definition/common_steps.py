from playwright.sync_api import Page, expect
from pytest_bdd import when, then, given, parsers
from basic_authentication_model.basic_authentication import BasicAuthentication
from config import BASE_URL
import os
import shutil


@given(parsers.parse('the user clicks the "{text}" button'))
@when(parsers.parse('the user clicks the "{text}" button'))
def click_button(page: Page, text):
    page.get_by_role("button", name=text).click()


@when(parsers.parse('the user clicks on the "{text}" button'))
@given(parsers.parse('the user clicks on the "{text}" tab'))
def click_on_tab(page: Page, text):
    page.get_by_role("link", name=text, exact=True).click()


downloaded_file = None
folder_path = "./tmp"


@when(parsers.parse('the user initiates the download by clicking "{button_text}"'))
def initiate_download(page: Page, button_text):
    global downloaded_file
    with page.expect_download() as download_info:
        page.get_by_role("link", name=button_text, exact=True).click()
    downloaded_file = download_info.value


@then('a zip file is downloaded')
def save_downloaded_file():
    file_path = f"{folder_path}/{downloaded_file.suggested_filename}"
    downloaded_file.save_as(file_path)

    # Check if the file has a .zip extension
    assert downloaded_file.suggested_filename.endswith(".zip")

    # Verify the file exists in the given folder
    assert os.path.exists(file_path)


@when('the tmp folder is deleted')
def delete_tmp_folder():
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)


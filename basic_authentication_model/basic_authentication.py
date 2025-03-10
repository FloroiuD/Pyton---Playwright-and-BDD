import base64
import os
from playwright.sync_api import Page


class BasicAuthentication:

    @staticmethod
    def execute(page: Page):
        username = os.environ.get('BASIC_AUTH_USERNAME')
        password = os.environ.get('BASIC_AUTH_PASSWORD')
        credentials = f"{username}:{password}"
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        authentication_header = f"Basic {encoded_credentials}"
        page.set_extra_http_headers({"Authorization": authentication_header})

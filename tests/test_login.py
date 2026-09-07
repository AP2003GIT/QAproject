import pytest
from playwright.sync_api import Page, expect

from data.users import INVALID_LOGIN_CASES, STANDARD_USER
from pages.login_page import LoginPage

def test_standard_user_can_log_in(
        login_page: LoginPage,
        page: Page,
) -> None:
    login_page.login(
        username=STANDARD_USER["username"],
        password=STANDARD_USER["password"],
    )

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

@pytest.mark.parametrize(
    "username, password, expected_message",
    INVALID_LOGIN_CASES,
)
def test_invalid_user_login_shows_error(
        login_page:LoginPage,
        username:str,
        password:str,
        expected_message:str,
) -> None:
    login_page.login(
        username = username,
        password = password,
    )

    expect(login_page.error_banner).to_contain_text(expected_message)
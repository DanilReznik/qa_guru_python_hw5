import pytest
import selene
from selene import browser, be, have


@pytest.fixture(scope="function", autouse=True)
def browser_conf():
    browser.config.base_url = "https://demoqa.com/automation-practice-form"
    browser.config.driver_name = "firefox"
    browser.config.timeout = 6.0
    browser.config.window_width = 1600
    browser.config.window_height = 800
    yield
    browser.quit()

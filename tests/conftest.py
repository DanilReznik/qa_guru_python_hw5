import pytest
from selene import browser


@pytest.fixture(scope="function")
def browser_conf():
    browser.config.base_url = "https://demoqa.com/automation-practice-form"
    browser.config.driver_name = "firefox"
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()

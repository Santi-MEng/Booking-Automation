import pytest
from utils.browser_setup import init_browser



@pytest.fixture(scope="function")
def set_driver():
    driver=init_browser()
    yield driver
    driver.delete_all_cookies()
    driver.close()


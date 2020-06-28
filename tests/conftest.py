import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver

    yield

    driver.quit()

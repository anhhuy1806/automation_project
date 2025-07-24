import pytest
from selenium import webdriver
import json

class BaseTest:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        request.cls.driver = self.driver
        yield
        self.driver.quit()

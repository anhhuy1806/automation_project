import pytest
import json
from pages.login_page import LoginPage
from base.base_test import BaseTest
from utils.config_reader import ConfigReader



#Successful Login

class TestLogin(BaseTest):
    def test_successful_login(self):
        with open("testsetting.json") as f:
            config = json.load(f)

        self.driver.get(config["base_url"])
        login = LoginPage(self.driver)
        login.login(config["username"], config["password"])

        assert "inventory" in self.driver.current_url

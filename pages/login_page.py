from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, username, password):
        self.type(self.username, username)
        self.type(self.password, password)
        self.click(self.login_button)

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )

    def click(self, locator):
        self.find(locator).click()

    def type(self, locator, text):
        self.find(locator).send_keys(text)

    def wait_until_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

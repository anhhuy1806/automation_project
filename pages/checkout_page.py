from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.firstname = (By.ID, "first-name")
        self.lastname = (By.ID, "last-name")
        self.zip = (By.ID, "postal-code")
        self.next = (By.ID, "continue")
        self.finish = (By.ID, "finish")
        self.confirm_message = (By.CLASS_NAME, "complete-header")

    def fill_checkout_info(self, fname, lname, zip):
        self.type(self.firstname, fname)
        self.type(self.lastname, lname)
        self.type(self.zip, zip)
        self.click(self.next)

    def finish_order(self):
        self.driver.execute_script("arguments[0].click();", self.find(self.finish))

    def get_confirmation_msg(self):
        return self.find(self.confirm_message).text
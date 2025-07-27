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
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.firstname)
        )
        self.type(self.firstname, fname)
        self.type(self.lastname, lname)
        self.type(self.zip, zip)
        self.click(self.next)

        # Wait until moved to step two
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("checkout-step-two")
        )

    def finish_order(self):
        print("Waiting for FINISH button to be clickable...")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.finish)
        )
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish)
        )
        print("FINISH button found. Clicking now.")
        self.driver.execute_script("arguments[0].click();", self.find(self.finish))

    def get_confirmation_msg(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.confirm_message)
        )
        return self.find(self.confirm_message).text

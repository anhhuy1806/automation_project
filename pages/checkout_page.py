from selenium.webdriver.common.by import By
from base.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(BasePage):
    FIRSTNAME = (By.ID, "first-name")
    LASTNAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")
    CONFIRM_MSG = (By.CLASS_NAME, "complete-header")

    def fill_checkout_info(self, fname, lname, zip):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.FIRSTNAME)
        )
        self.type(self.FIRSTNAME, fname)
        self.type(self.LASTNAME, lname)
        self.type(self.ZIP, zip)
        self.click(self.CONTINUE)

    def finish_order(self):
        print("Waiting for FINISH button to be clickable...")
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.FINISH)
        )
        print("FINISH button found. Clicking now.")
        self.driver.execute_script("arguments[0].click();", self.find(self.FINISH))

    def get_confirmation_msg(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.CONFIRM_MSG)
        )
        return self.find(self.CONFIRM_MSG).text

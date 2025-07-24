from selenium.webdriver.common.by import By
from base.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.add_button = (By.CLASS_NAME, "btn_inventory")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_products_to_cart(self, count=3):
        buttons = self.driver.find_elements(*self.add_button)[:count]
        for btn in buttons:
            btn.click()

    def go_to_cart(self):
        self.click(self.cart_icon)

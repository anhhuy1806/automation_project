from selenium.webdriver.common.by import By
from base.base_page import BasePage

class InventoryPage(BasePage):
    ADD_BTN = (By.CLASS_NAME, "btn_inventory")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_products_to_cart(self, count=3):
        buttons = self.driver.find_elements(*self.ADD_BTN)[:count]
        for btn in buttons:
            btn.click()

    def go_to_cart(self):
        self.click(self.CART_ICON)

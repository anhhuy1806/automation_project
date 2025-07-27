from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.add_button = (By.CLASS_NAME, "btn_inventory")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_products_to_cart(self, count=3):
        # Đợi đến khi các nút "Add to cart" có mặt
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.add_button)
        )

        buttons = self.driver.find_elements(*self.add_button)
        for btn in buttons[:count]:
            btn.click()

    def go_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_icon)
        )
        self.click(self.cart_icon)

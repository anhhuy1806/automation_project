import pytest
import json
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from base.base_test import BaseTest

class TestCheckout(BaseTest):
    def test_add_products_and_checkout(self):
        # Load config
        with open("testsetting.json") as f:
            config = json.load(f)

        self.driver.get(config["base_url"])

        # Login
        login = LoginPage(self.driver)
        login.login(config["username"], config["password"])

        # Add 3 items to cart
        inventory = InventoryPage(self.driver)
        inventory.add_products_to_cart(3)
        inventory.go_to_cart()

        # Go to checkout
        cart = CartPage(self.driver)
        cart.click_checkout()

        # Fill info
        checkout = CheckoutPage(self.driver)
        checkout.fill_checkout_info("John", "Doe", "70000")

        # Finish
        checkout.finish_order()

        # Verify
        msg = checkout.get_confirmation_msg()
        assert "Thank you for your order" in msg

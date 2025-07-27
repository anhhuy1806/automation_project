import pytest
from selenium import webdriver
import allure
import os
from datetime import datetime

class BaseTest:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self, method):
        test_name = method.__name__
        screenshot_dir = "screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)

        # Tên file ảnh theo timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_path = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")

        # Chụp ảnh khi test PASS hoặc FAIL
        self.driver.save_screenshot(screenshot_path)
        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name=test_name, attachment_type=allure.attachment_type.PNG)

        self.driver.quit()

import pytest
from selenium import webdriver
import allure
import os
from datetime import datetime
from utils.config_reader import ConfigReader

class BaseTest:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(ConfigReader.get_base_url())
        request.cls.driver = self.driver

        #tạo folder screenshots
        os.makedirs("screenshots", exist_ok=True)
        yield
        
        # Screenshot sau mỗi test (pass hoặc fail)
        test_name = request.node.name #lấy tên từ pytest
        filename = f"{test_name}.png" #tên_test.png
        filepath = os.path.join("screenshots", filename) #bỏ vào file screenshot
        self.driver.save_screenshot(filepath) #command screenshot
        allure.attach.file(filepath, name=test_name, attachment_type=allure.attachment_type.PNG) #add vào allure-result
        self.driver.quit()

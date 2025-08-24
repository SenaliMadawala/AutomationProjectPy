# tests/test_login_with_pages.py

import pytest
import sys
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage

class TestLoginWithPageObjects:

    def setup_method(self):
        """Setup method - runs before each test"""
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # Initialize page objects
        self.login_page = LoginPage(self.driver)

    def teardown_method(self):
        """Teardown method - runs after each test"""
        if hasattr(self, 'driver'):
            self.driver.quit()

    def test_valid_login_with_page_objects(self):
        """Test valid login using page objects"""
        # Perform login
        self.login_page.perform_login("tomsmith", "SuperSecretPassword!")

        # Verify login success
        assert self.login_page.is_login_successful(), "Login should be successful"
        assert self.login_page.is_logout_button_displayed(), "Logout button should be visible"

        print("✅ Valid login with page objects test passed!")

    def test_invalid_username_with_page_objects(self):
        """Test invalid username using page objects"""
        self.login_page.perform_login("invaliduser", "SuperSecretPassword!")

        assert self.login_page.is_login_failed(), "Login should fail"
        assert "Your username is invalid!" in self.login_page.get_error_message()

        print("✅ Invalid username with page objects test passed!")

    def test_invalid_password_with_page_objects(self):
        """Test invalid password using page objects"""
        self.login_page.perform_login("tomsmith", "wrongpassword")

        assert self.login_page.is_login_failed(), "Login should fail"
        assert "Your password is invalid!" in self.login_page.get_error_message()

        print("✅ Invalid password with page objects test passed!")

    @pytest.mark.parametrize("username,password,expected_message", [
        ("", "", "Your username is invalid!"),
        ("tomsmith", "", "Your password is invalid!"),
        ("", "SuperSecretPassword!", "Your username is invalid!"),
        ("wronguser", "wrongpass", "Your username is invalid!")
    ])
    def test_login_with_various_invalid_credentials(self, username, password, expected_message):
        """Test login with various invalid credential combinations"""
        self.login_page.perform_login(username, password)

        assert self.login_page.is_login_failed(), f"Login should fail for {username}/{password}"
        assert expected_message in self.login_page.get_error_message()

        print(f"✅ Test passed for credentials: {username}/{password}")
# tests/test_login.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestLogin:

    def setup_method(self):
        """Setup method - runs before each test"""
        # Setup Chrome driver using WebDriverManager
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        """Teardown method - runs after each test"""
        if hasattr(self, 'driver'):
            self.driver.quit()

    def test_valid_login(self):
        """Test login with valid credentials"""
        # Navigate to login page
        self.driver.get("http://the-internet.herokuapp.com/login")

        # Find elements and perform login
        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "[type='submit']")

        # Enter credentials
        username_field.send_keys("tomsmith")
        password_field.send_keys("SuperSecretPassword!")
        login_button.click()

        # Verify successful login
        success_message = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )

        assert "You logged into a secure area!" in success_message.text
        print("✅ Valid login test passed!")

    def test_invalid_username(self):
        """Test login with invalid username"""
        self.driver.get("http://the-internet.herokuapp.com/login")

        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "[type='submit']")

        username_field.send_keys("invaliduser")
        password_field.send_keys("SuperSecretPassword!")
        login_button.click()

        error_message = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error"))
        )

        assert "Your username is invalid!" in error_message.text
        print("✅ Invalid username test passed!")

    def test_invalid_password(self):
        """Test login with invalid password"""
        self.driver.get("http://the-internet.herokuapp.com/login")

        username_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, "[type='submit']")

        username_field.send_keys("tomsmith")
        password_field.send_keys("wrongpassword")
        login_button.click()

        error_message = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error"))
        )

        assert "Your password is invalid!" in error_message.text
        print("✅ Invalid password test passed!")

    def test_empty_credentials(self):
        """Test login with empty credentials"""
        self.driver.get("http://the-internet.herokuapp.com/login")

        login_button = self.driver.find_element(By.CSS_SELECTOR, "[type='submit']")
        login_button.click()

        error_message = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error"))
        )

        assert "Your username is invalid!" in error_message.text
        print("✅ Empty credentials test passed!")
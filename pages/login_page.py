# pages/login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Page Object Model for Login Page"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".flash.success")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".flash.error")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, ".button.secondary.radius")

    # Page Actions
    def navigate_to_login_page(self):
        """Navigate to the login page"""
        self.driver.get("http://the-internet.herokuapp.com/login")
        return self

    def enter_username(self, username):
        """Enter username in the username field"""
        username_field = self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD))
        username_field.clear()
        username_field.send_keys(username)
        return self

    def enter_password(self, password):
        """Enter password in the password field"""
        password_field = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD))
        password_field.clear()
        password_field.send_keys(password)
        return self

    def click_login_button(self):
        """Click the login button"""
        login_btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_btn.click()
        return self

    def get_success_message(self):
        """Get the success message text"""
        success_msg = self.wait.until(EC.presence_of_element_located(self.SUCCESS_MESSAGE))
        return success_msg.text

    def get_error_message(self):
        """Get the error message text"""
        error_msg = self.wait.until(EC.presence_of_element_located(self.ERROR_MESSAGE))
        return error_msg.text

    def is_logout_button_displayed(self):
        """Check if logout button is displayed"""
        try:
            logout_btn = self.wait.until(EC.presence_of_element_located(self.LOGOUT_BUTTON))
            return logout_btn.is_displayed()
        except:
            return False

    def perform_login(self, username, password):
        """Complete login flow - method chaining"""
        return (self.navigate_to_login_page()
                .enter_username(username)
                .enter_password(password)
                .click_login_button())

    def is_login_successful(self):
        """Check if login was successful"""
        try:
            success_message = self.get_success_message()
            return "You logged into a secure area!" in success_message
        except:
            return False

    def is_login_failed(self):
        """Check if login failed"""
        try:
            error_message = self.get_error_message()
            return ("Your username is invalid!" in error_message or
                    "Your password is invalid!" in error_message)
        except:
            return False
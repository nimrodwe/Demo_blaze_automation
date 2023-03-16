from src.utils.WebDriverSetup import WebDriverSetup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSignup(WebDriverSetup):

    def test_1_valid_signup(self):
        # signup a user
        self.signup_actions.signup_menu_button_action()
        self.signup_actions.username_action('userer213')
        self.signup_actions.password_action('userer213')
        self.signup_actions.signup_submit_button_action()
        # Wait for the alert to be present
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        # Wait for the login page to load and assert that the username field is visible
        alert_text = alert.text
        assert alert_text == 'Sign up successful.'

    def test_2_invalid_signup(self):
        self.signup_actions.signup_menu_button_action()
        self.signup_actions.username_action('B!@#!@$')
        self.signup_actions.password_action('D@!$@!%F')
        self.signup_actions.signup_submit_button_action()
        # Wait for the alert to be present
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        # Wait for the login page to load and assert that the username field is visible
        alert_text = alert.text
        assert alert_text == 'Wrong Credanitals.'

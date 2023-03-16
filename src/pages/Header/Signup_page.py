from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.Header.Signup_locator import Signup_locator

# basic signup actions which will help to signup
class SignupActions:
    def __init__(self, driver):
        self.driver = driver

    def signup_menu_button_action(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Signup_locator.signup_menu_button))).click()


    def username_action(self, username):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Signup_locator.signup_username_input))).send_keys(username)

    def password_action(self, password):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Signup_locator.signup_password_input))).send_keys(password)

    def signup_submit_button_action(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Signup_locator.signup_submit_button))).click()

    def cancel_button_action(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Signup_locator.signup_cancel_button))).click()



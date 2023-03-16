from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.Header.Login_Locator import Loginlocators


class Login:
    def __init__(self, driver):
        self.driver = driver

    def username_action(self, username):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Loginlocators.username_xpath))).send_keys(username)

    def password_action(self, password):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Loginlocators.password_xpath))).send_keys(password)

    def login_menu_btn(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Loginlocators.login_menu_button))).click()

    def login_button_action(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Loginlocators.loginbtn_xpath))).click()

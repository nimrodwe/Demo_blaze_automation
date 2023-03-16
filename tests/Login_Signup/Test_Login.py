from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.utils.WebDriverSetup import WebDriverSetup


class TestLogin(WebDriverSetup):
    # valid login
    def test_1_valid_login(self):
        self.login_actions.login_menu_btn()
        self.login_actions.username_action('nimrod')
        self.login_actions.password_action('nimrod')
        self.login_actions.login_button_action()
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[''@id'
                                                                                                  '="nameofuser"]')))
        self.assertTrue(element)

    # negative login and should get a fail unittest
    def test_2_invalid_login(self):
        self.login_actions.login_menu_btn()
        self.login_actions.username_action('baduser')
        self.login_actions.password_action('baduser')
        self.login_actions.login_button_action()
        element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[''@id'
                                                                                                  '="nameofuser"]')))
        self.assertTrue(element)

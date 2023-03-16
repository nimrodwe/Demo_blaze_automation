from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.utils.WebDriverSetup import WebDriverSetup
from selenium.webdriver.support import expected_conditions as EC


class TestLogout(WebDriverSetup):

    def test_1_logout(self):
        self.login_actions.login_menu_btn()
        self.login_actions.username_action('nimrod')
        self.login_actions.password_action('nimrod')
        self.login_actions.login_button_action()
        self.menu_clicking.logout_click()
        login_check_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login2"]')))
        self.assertTrue(login_check_element)


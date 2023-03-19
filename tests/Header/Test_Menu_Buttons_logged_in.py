import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from src.utils.WebDriverSetup import WebDriverSetup


class TestMenuButtons(WebDriverSetup):
    def test_1_home_button(self):
        # login to user
        self.login_actions.login_menu_btn()
        self.login_actions.username_action('nimrod')
        self.login_actions.password_action('nimrod')
        self.login_actions.login_button_action()
        time.sleep(2)
        self.menu_clicking.home_click()
        assert self.driver.current_url == 'https://demoblaze.com/index.html'

    def test_2_about_us_button(self):
        # login to user
        self.login_actions.login_menu_btn()
        self.login_actions.username_action('nimrod')
        self.login_actions.password_action('nimrod')
        self.login_actions.login_button_action()
        time.sleep(2)
        self.menu_clicking.about_us_click()
        about_us_validate = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="example-video"]/div[1]')))
        self.assertTrue(about_us_validate)

    def test_3_contact_button(self):
        # login to user
        self.login_actions.login_menu_btn()
        self.login_actions.username_action('nimrod')
        self.login_actions.password_action('nimrod')
        self.login_actions.login_button_action()
        time.sleep(2)
        self.menu_clicking.contact_click()
        # check for xpath inside the pop
        contact_validate = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="exampleModalLabel"]')))
        self.assertTrue(contact_validate)

    def test_4_cart_button(self):
        # login to user
        self.login_actions.login_menu_btn()
        self.login_actions.username_action('nimrod')
        self.login_actions.password_action('nimrod')
        self.login_actions.login_button_action()
        time.sleep(2)
        self.menu_clicking.cart_click()
        # check if the page domain is true
        assert self.driver.current_url == 'https://demoblaze.com/cart.html'

    def test_5_Welcome_user(self):
        # login to user
        self.login_actions.login_menu_btn()
        self.login_actions.username_action('nimrod')
        self.login_actions.password_action('nimrod')
        self.login_actions.login_button_action()
        time.sleep(2)
        self.menu_clicking.welcome_user_click()
        welcome_user_validate = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.ID, 'user-information')))
        self.assertTrue(welcome_user_validate)





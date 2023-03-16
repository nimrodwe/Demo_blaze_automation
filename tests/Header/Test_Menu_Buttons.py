from src.utils.WebDriverSetup import WebDriverSetup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class TestHome(WebDriverSetup):

    def test_1_home_btn(self):
        # click menu home button
        self.menu_clicking.home_click()
        # check if it sends to proper domain
        assert self.driver.current_url == 'https://demoblaze.com/index.html'

    def test_2_contact_btn(self):
        # click menu contact button
        self.menu_clicking.contact_click()
        # takes the element text inside the contact menu
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="exampleModalLabel"]')))
        # check if it's there
        self.assertTrue(element)

    def test_3_about_us_btn(self):
        # click about us button in the menu
        self.menu_clicking.about_us_click()
        # takes the element text inside the about us menu
        element = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="example-video"]/div[1]')))
        # checks if it's there
        self.assertTrue(element)

    def test_4_cart(self):
        # click the cart button in the menu
        self.menu_clicking.cart_click()
        # checks if it's there
        assert self.driver.current_url == 'https://demoblaze.com/cart.html'

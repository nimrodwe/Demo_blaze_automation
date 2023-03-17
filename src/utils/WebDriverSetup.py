import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from src.pages.Header.Menu_button_click import MenuButtonsAction
from src.pages.Header.Login_page import Login
from src.pages.Header.Signup_page import SignupActions
from src.pages.Cart_Page import CartActions
from src.pages.Homepage.Item_Card_Page import ItemCardActions
from src.pages.Homepage.RIght_Left_Arrow_Page import ArrowActions


class WebDriverSetup(unittest.TestCase):

    def setUp(self) -> None:
        try:
            chromedriver_path = "chromedriver.exe"
            service = Service(executable_path=chromedriver_path)
            options = Options()
            options.headless = False
            options.add_argument("--disable-extensions")
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.maximize_window()
            self.driver.set_page_load_timeout(30)
            self.driver.get("https://demoblaze.com/index.html")
            self.menu_clicking = MenuButtonsAction(self.driver)
            self.login_actions = Login(self.driver)
            self.signup_actions = SignupActions(self.driver)
            self.cart_action = CartActions(self.driver)
            self.item_card_actions = ItemCardActions(self.driver)
            self.arrow_action = ArrowActions(self.driver)


            time.sleep(1)

        except AssertionError:
            self.driver.quit()

    def tearDown(self) -> None:
        self.driver.quit()

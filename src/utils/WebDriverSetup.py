import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from src.pages.Header.Menu_button_click import MenuButtonsAction
from src.pages.Header.Login_page import Login
from src.pages.Header.Signup_page import SignupActions


class WebDriverSetup(unittest.TestCase):

    def setUp(self) -> None:
        try:
            chromedriver_path = "chromedriver.exe"
            service = Service(executable_path=chromedriver_path)
            options = Options()
            options.headless = True
            options.add_argument("--disable-extensions")
            self.driver = webdriver.Chrome(service=service, options=options)
            self.driver.maximize_window()
            self.driver.set_page_load_timeout(30)
            self.driver.get("https://demoblaze.com/index.html")
            self.menu_clicking = MenuButtonsAction(self.driver)
            self.login_actions = Login(self.driver)
            self.signup_actions = SignupActions(self.driver)


            time.sleep(1)

        except AssertionError:
            self.driver.quit()

    def tearDown(self) -> None:
        self.driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.Header.Menu_Locator import Menulocator


class MenuButtonsAction:
    def __init__(self,driver):
        self.driver = driver

    def home_click(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Menulocator.home_locator))).click()

    def contact_click(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Menulocator.contact_locator))).click()

    def about_us_click(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Menulocator.about_us_locator))).click()

    def cart_click(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Menulocator.cart_locator))).click()

    def logout_click(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Menulocator.logout_locator))).click()

    def icon_click(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, Menulocator.icon_locator))).click()



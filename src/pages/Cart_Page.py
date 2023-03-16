from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.Cart_Locator import CartLocators


class CartActions:
    def __init__(self, driver):
        self.driver = driver

    def place_order_action(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, CartLocators.place_order_button))).click()

    def form_name_action(self, name):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, CartLocators.name))).send_keys(name)

    def form_country_action(self, country):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, CartLocators.country))).send_keys(country)

    def form_city_action(self, city):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, CartLocators.city))).send_keys(city)

    def form_credit_card_action(self, credit_card):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, CartLocators.credit_card))).send_keys(credit_card)

    def form_month_action(self, month):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, CartLocators.month))).send_keys(month)

    def form_year_action(self, year):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, CartLocators.year))).send_keys(year)

    def form_submit_button_action(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, CartLocators.form_purchase_button))).click()
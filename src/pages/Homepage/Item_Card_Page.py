from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.Homepage.Item_Card_Locator import ItemCardLocator
from src.locators.Homepage.Item_Prodpage_Locator import ItemProdpage_Locator

class ItemCardActions:
    def __init__(self, driver):
        self.driver = driver

    def item_image_click(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, ItemCardLocator.item_image))).click()

    def item_add_to_cart(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, ItemProdpage_Locator.add_to_cart_button))).click()

    def item_name_visual(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, ItemProdpage_Locator.item_name)))
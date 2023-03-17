import time

from src.utils.WebDriverSetup import WebDriverSetup
from src.locators.Homepage.Item_Prodpage_Locator import ItemProdpage_Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestItemProdPage(WebDriverSetup):
    def test_1_item_prodpage_visual(self):
        self.item_card_actions.item_image_click()
        name_xpath = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*['
                                                                                                     '@id="tbodyid"]/h3')))
        self.assertTrue(name_xpath)

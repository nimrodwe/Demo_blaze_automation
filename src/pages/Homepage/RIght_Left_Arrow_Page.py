from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.Homepage.Right_Left_Arrow_Locators import RightLeftArrow

class ArrowActions:
    def __init__(self, driver):
        self.driver = driver

    def right_arrow_action(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, RightLeftArrow.right_arrow))).click()

    def left_arrow_action(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, RightLeftArrow.left_arrow))).click()
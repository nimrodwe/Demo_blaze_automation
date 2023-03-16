from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.utils.WebDriverSetup import WebDriverSetup
from selenium.webdriver.support import expected_conditions as EC

class TestSanityPurchaseItem(WebDriverSetup):

    def test_1_purchase_item(self):
        # pick an item image from the homepage container
        self.item_card_actions.item_image_click()
        # add item to cart
        self.item_card_actions.item_add_to_cart()
        # accept alert prompt
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()
        # enter cart page
        self.menu_clicking.cart_click()
        # clicking the press order button
        self.cart_action.place_order_action()
        # entering name to input
        self.cart_action.form_name_action("nimrod")
        # entering country to input
        self.cart_action.form_country_action("israel")
        # entering city to input
        self.cart_action.form_city_action("tel-aviv")
        # entering credit card to input
        self.cart_action.form_credit_card_action("12334-3124-24155")
        # entering month to input
        self.cart_action.form_month_action("12")
        # entering year to input
        self.cart_action.form_year_action('1999')
        # submitting purchase
        self.cart_action.form_submit_button_action()
        verify_purchase = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[10]/h2')))
        self.assertTrue(verify_purchase)



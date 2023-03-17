from src.utils.WebDriverSetup import WebDriverSetup


class TestIcon(WebDriverSetup):

    def test_1_test_icon(self):
        self.menu_clicking.icon_click()
        assert self.driver.current_url == 'https://demoblaze.com/index.html'

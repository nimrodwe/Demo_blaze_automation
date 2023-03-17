from src.utils.WebDriverSetup import WebDriverSetup

class TestRightLeftArrow(WebDriverSetup):

    def test_1_right_arrow(self):
        self.arrow_action.right_arrow_action()
        arrow_action_validate = '//*[@id="carouselExampleIndicators"]/div/div[2]/img'
        self.assertTrue(arrow_action_validate)

    def test_2_left_arrow(self):
        self.arrow_action.left_arrow_action()
        arrow_action_validate = '//*[@id="carouselExampleIndicators"]/div/div[3]/img'
        self.assertTrue(arrow_action_validate)
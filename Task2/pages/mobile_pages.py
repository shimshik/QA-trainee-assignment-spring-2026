from pages.base_page import BasePage
from pages.locators.mobile_page_locators import MobilePageLocators
class MobilePage(BasePage):

    def change_theme(self):
        self.click(MobilePageLocators.BUTTON_CHANGE_THEME)

    def get_theme_value(self):
        return self.get_theme(MobilePageLocators.HTML_HEAD)

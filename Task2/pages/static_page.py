from pages.base_page import BasePage
from pages.locators.static_page_locators import StaticPageLocator
from selenium.common.exceptions import NoSuchElementException,TimeoutException

class StaticPage(BasePage):

    def click_static_page(self):
        self.click(StaticPageLocator.STATIC_PAGE)

    def click_refresh_button(self):
        self.click(StaticPageLocator.REFRESH_BUTTON)

    def click_stop_button(self):
        self.click(StaticPageLocator.STOP_TIMER_BUTTON)

    def click_activate_button(self):
        self.click(StaticPageLocator.ACTIVATE_TIMER_BUTTON)

    def get_time(self):
        return self.get_text(StaticPageLocator.TIMER)

    def get_message(self):
        try:
            if self.get_text(StaticPageLocator.DISABLED_TIMER_MESSAGE):
                return True
        except NoSuchElementException:
            return False

    def is_timer_visible(self):
        try:
            if self.find_element(StaticPageLocator.TIMER):
                return True
        except TimeoutException:
            return False
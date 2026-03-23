import pytest
from conftest import mobile_driver
from pages.mobile_pages import MobilePage


class TestMobilePages:

    def test_change_on_light_theme(self,mobile_driver):#17
        mobile_page = MobilePage(mobile_driver)
        mobile_page.change_theme()
        theme = mobile_page.get_theme_value()

        assert theme == 'light' , f"Тема не изменилась, текущая тема {theme}"


    def test_change_on_dark_theme(self,mobile_driver):#18
        mobile_page = MobilePage(mobile_driver)
        mobile_page.change_theme()
        mobile_page.change_theme()
        theme = mobile_page.get_theme_value()

        assert theme == 'dark' , f"Тема не изменилась, текущая тема {theme}"
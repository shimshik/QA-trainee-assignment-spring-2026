import pytest
from conftest import driver
from pages.static_page import StaticPage
import time

class TestStaticPage:

    def test_refresh_button(self,driver):#14
        static_page = StaticPage(driver)
        static_page.click_static_page()
        time.sleep(5)
        static_page.click_refresh_button()
        timer_value = static_page.get_time()
        assert timer_value == '5:00' , 'Кнопка "Обновить" не обновляет значение таймера до начального(5 минут)'

    def test_stop_timer_button(self,driver):#15
        static_page = StaticPage(driver)
        static_page.click_static_page()
        static_page.click_stop_button()
        message = static_page.get_message()

        assert message == True, "Не отображается сообщение о отключении автообновления"

    def test_activate_timer_button(self, driver):#16
        static_page = StaticPage(driver)
        static_page.click_static_page()
        static_page.click_stop_button()
        static_page.click_activate_button()
        if static_page.is_timer_visible():
            timer_value = static_page.get_time()
            assert timer_value == '5:00', 'Таймер после снятия с паузы автообновления не обновляет свое значение до начального(5 минут)'
        else:
            assert False, "Таймер не отображается после снятия с паузы автообновления"



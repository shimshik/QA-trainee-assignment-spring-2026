from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import logging


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)
        self.logger = logging.getLogger(type(self).__name__)



    def find_element(self, locator, timeout: int = None):

        wait_time = timeout or self.timeout
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located(locator)
            )
            self.logger.debug(f"Элемент найден: {locator}")
            return element
        except TimeoutException:
            self.logger.error(f"Элемент не найден за {wait_time}с: {locator}")

            self.take_screenshot("element_not_found")
            raise

    def find_elements(self, locator, timeout: int = None, refresh: bool = False) -> list:
        wait_time = timeout or self.timeout

        try:
            if refresh:
                pass

            elements = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_all_elements_located(*locator)
            )
            self.logger.debug(f"Найдено элементов {len(elements)}: {locator}")
            return elements
        except TimeoutException:
            self.logger.error(f"Элементы не найдены за {wait_time}с: {locator}")
            return []

    def find_clickable_element(self, locator, timeout: int = None) -> WebElement:

        wait_time = timeout or self.timeout
        return WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator: tuple, timeout: int = None):

        element = self.find_clickable_element(locator, timeout)
        element.click()
        self.logger.debug(f"Клик по элементу: {locator}")

    def type_text(self, locator: tuple, text: str, timeout: int = None):

        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        self.logger.debug(f"Введен текст '{text}' в {locator}")

    def get_text(self, locator: tuple, timeout: int = None) -> str:

        element = self.find_element(locator, timeout)
        text = element.text
        self.logger.debug(f"Получен текст: '{text}' из {locator}")
        return text

    def is_element_present(self, locator: tuple, timeout: int = None) -> bool:

        try:
            self.find_element(locator, timeout or 5)
            return True
        except TimeoutException:
            return False

    def is_element_visible(self, locator: tuple) -> bool:

        try:
            element = self.find_element(locator, 5)
            return element.is_displayed()
        except:
            return False

    def is_element_clickable(self, locator, timeout: int = 5) -> bool:
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            return True
        except:
            return False



    def open(self, url: str):

        self.driver.get(url)
        self.logger.debug(f"Открыт URL: {url}")

    def get_current_url(self) -> str:

        return self.driver.current_url

    def get_title(self) -> str:

        return self.driver.title

    def refresh(self):

        self.driver.refresh()
        self.logger.debug("Страница обновлена")

    def back(self):

        self.driver.back()
        self.logger.debug("Переход назад")

    def forward(self):

        self.driver.forward()
        self.logger.debug("Переход вперед")


    def take_screenshot(self, name: str = "screenshot"):

        timestamp = self._get_timestamp()
        filename = f"{name}_{timestamp}.png"
        self.driver.save_screenshot(filename)
        self.logger.info(f"Скриншот сохранен: {filename}")
        return filename

    def _get_timestamp(self):

        from datetime import datetime
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    def get_theme(self,locator : tuple):
        element = self.find_element(locator)
        return element.get_attribute("data-theme")

    def scroll_to_element(self, locator: tuple):

        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.logger.debug(f"Скролл к элементу: {locator}")

    def wait_for_url_changes(self, old_url: str, timeout: int = 10):

        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.current_url != old_url
            )
            self.logger.debug("URL изменился")
        except TimeoutException:
            self.logger.error(f"URL не изменился за {timeout}с. Старый URL: {old_url}")
            raise

    def switch_to_new_window(self, timeout: int = 10):
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > 1
        )
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                self.logger.debug(f"Переключились на новую вкладку: {window_handle}")
                return
        raise Exception("Новая вкладка не найдена")

    def close_current_window_and_switch_back(self, original_window: str = None):
        if not original_window:
            original_window = self.driver.window_handles[0]
        self.driver.close()
        self.driver.switch_to.window(original_window)
        self.logger.debug("Закрыли текущую вкладку и вернулись на исходную")

    def scroll_slider_horizontally(self, slider_locator: tuple, direction, pixels):

        slider = self.find_element(slider_locator)

        if direction == "right":
            self.driver.execute_script("arguments[0].scrollLeft += arguments[1];", slider, pixels)
        elif direction == "left":
            self.driver.execute_script("arguments[0].scrollLeft -= arguments[1];", slider, pixels)
        else:
            raise ValueError("direction должен быть 'right' или 'left'")

        self.logger.debug(f"Скролл слайдера {direction} на {pixels}px")

    def scroll_vertical_by_pixels(self, pixels: int = 500):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def select_all_text(self, locator: tuple):

        element = self.find_element(locator)
        element.send_keys(Keys.CONTROL, 'a')

    def send_keys_to_element(self, locator: tuple, keys):

        element = self.find_element(locator)
        element.send_keys(keys)

    def get_error_messages(self, error_locator: tuple) -> list:

        errors = self.find_elements(error_locator)
        return [error.text for error in errors]

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='test_logs.log',
        filemode='w'
    )

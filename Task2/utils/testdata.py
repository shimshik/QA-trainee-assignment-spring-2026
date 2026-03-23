from pages.locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import re
from conftest import driver

class PriceGetter:

    @staticmethod
    def collect_all_prices_across_pages(driver):
        all_prices = []
        page_number = 1

        while True:
            # Собрать цены на текущей странице
            page_prices = PriceGetter.collect_prices_from_current_page(driver)
            all_prices.extend(page_prices)
            if not PriceGetter.go_to_next_page(driver):
                break

            page_number += 1
            if page_number == 3:
                return all_prices

        return all_prices

    @staticmethod
    def collect_prices_from_current_page(driver):
        prices = []
        try:
            for i in range(len(MainPageLocators.ANNOUNCEMENT_PRICE)):
                price_element = driver.find_element(*MainPageLocators.ANNOUNCEMENT_PRICE[i])
                price_text = price_element.text
                clean_price = re.sub(r'[^0-9]', '', price_text)

                if clean_price:
                        prices.append(int(clean_price))
        except NoSuchElementException:
            pass
        return prices

    @staticmethod
    def go_to_next_page(driver):
        try:
            next_button = driver.find_element(*MainPageLocators.NEXT_PAGE_BUTTON)
            next_button.click()

            WebDriverWait(driver, 0)


            return True



        except TimeoutException:
            return False

    @staticmethod
    def min_filtered_price(prices,filter_min_price,driver):
        for i in range(len(prices)):
            if prices[i] >= filter_min_price:
                return prices[i]
        return None

    @staticmethod
    def max_filtered_price(prices,filter_max_price, driver):
        for i in range(len(prices)-1,-1,-1):
            if prices[i] <= filter_max_price:
                return prices[i]
        return None

class CardCategoryGetter:
    @staticmethod
    def get_all_cards_category_from_current_page(driver):
        category = []
        try:
            for i in range(len(MainPageLocators.ANNOUNCEMENT_TITLE)):
                cards_element = driver.find_element(*MainPageLocators.ANNOUNCEMENT_TITLE[i])
                cards_text = cards_element.text

                if cards_text:
                    category.append(cards_text)
        except NoSuchElementException:
            pass
        return category

    @staticmethod
    def collect_all_category_across_pages(driver):
        all_category = []
        page_number = 1

        while True:
            # Собрать цены на текущей странице
            page_category = CardCategoryGetter.get_all_cards_category_from_current_page(driver)
            all_category.extend(page_category)
            if not PriceGetter.go_to_next_page(driver):
                break

            page_number += 1
            if page_number == 3:
                return all_category

        return all_category

class CardGetter:
    @staticmethod
    def get_all_cards_from_current_page(driver):
        cards = []
        try:
            for i in range(len(MainPageLocators.ANNOUNCEMENT_CARD)):
                cards_element = driver.find_element(*MainPageLocators.ANNOUNCEMENT_CARD[i])
                cards.append(cards_element)
        except NoSuchElementException:
            pass
        return cards

    @staticmethod
    def collect_all_card_across_pages(driver):
        all_cards = []
        page_number = 1

        while True:
            # Собрать цены на текущей странице
            page_cards = CardGetter.get_all_cards_from_current_page(driver)
            all_cards.extend(page_cards)
            if not PriceGetter.go_to_next_page(driver):
                break

            page_number += 1
            if page_number == 3:
                return all_cards

        return all_cards

class TestdataFilter:

    from_up_to_range = [[1000,10000],[20000,40000],[10000,70000]]

    from_range = [1000,10000,5000]

    up_to_range = [10000,20000,60000]

    negative_value_from_up_to = [[-1,-1000],[-5000,-1000],[-1000,-1000000]]

    negative_value_from = [-1,-1000,-20000]

    negative_value_up_to = [-1,-1000,-100000]

    negative_value_from_positive_value_up_to = [[-100,10000],[-1,5000],[-10000,10000]]

    positive_value_from_negative_value_up_to = [[100, -10000], [1, -5000], [3000, -10000]]

    sorting_options = ['desc','asc']

    category_type = ['0','1','2','3','4','5','6','7']
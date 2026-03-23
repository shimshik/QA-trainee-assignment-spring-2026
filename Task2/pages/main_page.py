from pages.base_page import BasePage
from pages.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def click_sorting_type_dropdown(self):
        self.click(MainPageLocators.SORTING_TYPE_DROPDOWN)

    def click_sorting_order_dropdown(self):
        self.click(MainPageLocators.SORTING_ORDER_DROPDOWN)

    def click_category_dropdown(self):
        self.click(MainPageLocators.CATEGORY_DROPDOWN)

    def enter_price_filter_from(self,price):
        self.send_keys_to_element(MainPageLocators.PRICE_RANGE_FROM,price)

    def enter_price_filter_up_to(self,price):
        self.send_keys_to_element(MainPageLocators.PRICE_RANGE_UP_TO,price)

    def click_priority_toggle(self):
        self.click(MainPageLocators.PRIORITY_TOGGLE)

    def click_status_on_moderation(self):
        self.click(MainPageLocators.MODERATION_STATUS)

    def click_status_approved(self):
        self.click(MainPageLocators.APPROVED_STATUS)

    def click_status_denied(self):
        self.click(MainPageLocators.DENIED_STATUS)

    def click_status_draft(self):
        self.click(MainPageLocators.DRAFT_STATUS)

    def click_dropdown_option(self,value):
        locator = MainPageLocators.dropdown_value_locator(value)
        self.click(locator)

    def click_first_page_button(self):
        self.click(MainPageLocators.FIRST_PAGE_BUTTON)

    def is_empty_message_visible(self):
        return self.is_element_visible(MainPageLocators.EMPTY_DASHBOARD_MESSAGE)

    def choose_sorting_type(self,value):
        self.click(MainPageLocators.dropdown_value_locator(value))

    def choose_sorting_order(self,value):
        self.click(MainPageLocators.dropdown_value_locator(value))

    def choose_category(self,value):
        self.click(MainPageLocators.dropdown_value_locator(value))

    def get_sorting_by_price(self):
        self.click_sorting_type_dropdown()
        self.choose_sorting_type('price')
        self.choose_sorting_order('desc')

    @staticmethod
    def verify_all_cards_have_priority(cards):
        for card in cards:
            priority_element = card.find_elements(*MainPageLocators.PRIORITY_BADGE)

            if not priority_element:
                return False
        return True

    @staticmethod
    def check_price_filter_for_currents_cards(min_price, max_price, current_prices):
        flag = True
        for i in range(len(current_prices)):
            if not (min_price <= current_prices[i] <= max_price):
                flag = False
            else:
                flag = True
        return flag

    @staticmethod
    def check_all_good_cards_on_dashboard_price_filter(min_price, max_price, current_prices,all_prices):
        flag = True
        for i in range(len(all_prices)):
            if not ((min_price <= all_prices[i] <= max_price) and (all_prices[i] in current_prices)):
                return False
        return flag

    @staticmethod
    def check_price_filter_from(min_price,current_prices):
        flag = True
        for i in range(len(current_prices)):
            if not (min_price <= current_prices[i]):
                flag = False
            else:
                flag = True
        return flag

    @staticmethod
    def check_price_filter_from_all_good_cards_on_dashboard(min_price, current_prices,all_prices):
        flag = True
        for i in range(len(all_prices)):
            if not ((all_prices[i] >= min_price) and (all_prices[i] in current_prices)):
                flag = False

        return flag

    @staticmethod
    def check_price_filter_up_to(max_price, current_prices):
        flag = True
        for i in range(len(current_prices)):
            if not (max_price >= current_prices[i]):
                flag = False
            else:
                flag = True
        return flag

    @staticmethod
    def check_price_filter_up_to_all_good_cards_on_dashboard(max_price, current_prices, all_prices):
        flag = True
        for i in range(len(all_prices)):
            if not ((all_prices[i] <= max_price) and (all_prices[i] in current_prices)):
                flag = False

        return flag

    @staticmethod
    def check_category(value,text):
        match value:
            case '0':
                return 'Электроника' in text
            case '1':
                return 'Недвижимость' in text
            case '2':
                return 'Транспорт' in text
            case '3':
                return 'Работа' in text
            case '4':
                return 'Услуги' in text
            case '5':
                return 'Животные' in text
            case '6':
                return 'Мода' in text
            case '7':
                return 'Детское' in text

            case _:
                return False

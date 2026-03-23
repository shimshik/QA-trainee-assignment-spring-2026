import time

import pytest
from utils.testdata import PriceGetter,CardCategoryGetter,CardGetter, TestdataFilter
from conftest import driver
from pages.main_page import MainPage


class TestMainPage:

    @pytest.mark.parametrize('price_from,price_up_to',
                             TestdataFilter.from_up_to_range
                             )
    def test_price_filter_from_up_to(self,driver,price_from,price_up_to): #1
        main_page = MainPage(driver)
        all_prices = (sorted(PriceGetter.collect_all_prices_across_pages(driver)))
        main_page.click_first_page_button()
        main_page.enter_price_filter_from(price_from)
        main_page.enter_price_filter_up_to(price_up_to)
        current_prices = sorted(PriceGetter.collect_all_prices_across_pages(driver))
        result1 = main_page.check_price_filter_for_currents_cards(price_from,price_up_to,current_prices)
        result2 = main_page.check_all_good_cards_on_dashboard_price_filter(price_from,price_up_to,current_prices,all_prices)
        if not (result2!=True or result1!=True):
            assert False, (f'В выдаче есть объявление вне фильтра ценового диапозона, '
                           f'В выдаче есть не все объявление проходящие фильтр ценового диапозона')
        else:
            if not result1:
                assert result2 == True, f'В выдаче есть не все объявление проходящие фильтр ценового диапозона'
            elif not result2:
                assert False, (f'В выдаче есть объявление вне фильтра ценового диапозона, '
                               f'В выдаче есть не все объявление проходящие фильтр ценового диапозона')

    @pytest.mark.parametrize('price_from,',
                             TestdataFilter.from_range
                             )
    def test_price_filter_from(self,driver,price_from): #2
        main_page = MainPage(driver)
        all_prices = (sorted(PriceGetter.collect_all_prices_across_pages(driver)))
        main_page.click_first_page_button()
        main_page.enter_price_filter_from(price_from)
        current_prices = sorted(PriceGetter.collect_all_prices_across_pages(driver))
        result1 = main_page.check_price_filter_from(price_from,current_prices)
        result2 = main_page.check_price_filter_from_all_good_cards_on_dashboard(price_from,current_prices,all_prices)

        if not (result2 != True or result1 != True):
            assert False, (f'В выдаче есть объявление вне фильтра ценового диапозона, '
                           f'В выдаче есть не все объявление проходящие фильтр ценового диапозона')
        else:
            if not result1:
                assert result2 == True, f'В выдаче есть не все объявление проходящие фильтр ценового диапозона'
            elif not result2:
                assert False, (f'В выдаче есть объявление вне фильтра ценового диапозона, '
                               f'В выдаче есть не все объявление проходящие фильтр ценового диапозона')

    @pytest.mark.parametrize('price_up_to,',
                             TestdataFilter.up_to_range
                             )
    def test_price_filter_up_to(self, driver, price_up_to): #3
        main_page = MainPage(driver)
        all_prices = (sorted(PriceGetter.collect_all_prices_across_pages(driver)))
        main_page.click_first_page_button()
        main_page.enter_price_filter_up_to(price_up_to)
        current_prices = (sorted(PriceGetter.collect_all_prices_across_pages(driver)))
        result1 = main_page.check_price_filter_up_to(price_up_to, current_prices)
        result2 = main_page.check_price_filter_up_to_all_good_cards_on_dashboard(price_up_to, current_prices, all_prices)

        if not (result2 != True or result1 != True):
            assert False, (f'В выдаче есть объявление вне фильтра ценового диапозона, '
                           f'В выдаче есть не все объявление проходящие фильтр ценового диапозона')
        else:
            if not result1:
                assert result2 == True, f'В выдаче есть не все объявление проходящие фильтр ценового диапозона'
            elif not result2:
                assert False, (f'В выдаче есть объявление вне фильтра ценового диапозона, '
                               f'В выдаче есть не все объявление проходящие фильтр ценового диапозона')

    @pytest.mark.parametrize('price_from,price_up_to',
                             TestdataFilter.negative_value_from_up_to
                             )
    def test_price_filter_negative_value(self,driver,price_from,price_up_to): #4
        main_page = MainPage(driver)
        main_page.enter_price_filter_from(price_from)
        main_page.enter_price_filter_up_to(price_up_to)
        flag = main_page.is_empty_message_visible()
        assert flag , "На доске не появилось сообщение 'Объявления не найдены'"

    @pytest.mark.parametrize('price_from',
                             TestdataFilter.negative_value_from
                             )
    def test_price_filter_negative_value_from(self, driver, price_from): #5
        main_page = MainPage(driver)
        all_prices = (sorted(PriceGetter.collect_all_prices_across_pages(driver)))
        main_page.click_first_page_button()
        main_page.enter_price_filter_from(price_from)
        current_prices = (sorted(PriceGetter.collect_all_prices_across_pages(driver)))
        flag = False
        if current_prices == all_prices:
            flag = True

        assert flag, "Система неверно интерпритирует негативные числа в поле От(т.е. не как 0)"

    @pytest.mark.parametrize('price_up_to',
                             TestdataFilter.negative_value_up_to
                             )
    def test_price_filter_negative_value_up_to(self, driver,price_up_to): #6
        main_page = MainPage(driver)
        main_page.enter_price_filter_up_to(price_up_to)
        flag = main_page.is_empty_message_visible()
        assert flag, "На доске не появилось сообщение 'Объявления не найдены'"

    @pytest.mark.parametrize('price_from,price_up_to',
                             TestdataFilter.negative_value_from_positive_value_up_to
                             )
    def test_price_filter_negative_from_positive_up_to_value(self,driver,price_from,price_up_to):#7
        main_page = MainPage(driver)
        all_prices = (sorted(PriceGetter.collect_all_prices_across_pages(driver)))
        main_page.click_first_page_button()
        main_page.enter_price_filter_from(price_from)
        main_page.enter_price_filter_up_to(price_up_to)
        current_prices = sorted(PriceGetter.collect_all_prices_across_pages(driver))
        result1 = main_page.check_price_filter_for_currents_cards(price_from,price_up_to,
                                                                  current_prices)
        result2 = main_page.check_all_good_cards_on_dashboard_price_filter(price_from,price_up_to,
                                                                           current_prices, all_prices)
        if not (result2 != True or result1 != True):
            assert False, (f'В выдаче есть объявление вне фильтра ценового диапозона, '
                           f'В выдаче есть не все объявление проходящие фильтр ценового диапозона')
        else:
            if not result1:
                assert result2 == True, f'В выдаче есть не все объявление проходящие фильтр ценового диапозона'
            elif not result2:
                assert False, (f'В выдаче есть объявление вне фильтра ценового диапозона, '
                               f'В выдаче есть не все объявление проходящие фильтр ценового диапозона')

    @pytest.mark.parametrize('price_from,price_up_to',
                             TestdataFilter.positive_value_from_negative_value_up_to
                             )
    def test_price_filter_positive_from_negative_up_to_value(self, driver, price_from, price_up_to):#8
        main_page = MainPage(driver)
        main_page.enter_price_filter_from(price_from)
        main_page.enter_price_filter_up_to(price_up_to)

        flag = main_page.is_empty_message_visible()
        assert flag, "На доске не появилось сообщение 'Объявления не найдены'"

    @pytest.mark.parametrize('value',
                             TestdataFilter.sorting_options
                             )
    def test_sorting_by_price(self,driver,value):#10-11
        main_page = MainPage(driver)
        main_page.click_sorting_type_dropdown()
        main_page.choose_sorting_type('price')
        main_page.choose_sorting_order(value)
        current_prices = (PriceGetter.collect_all_prices_across_pages(driver))

        if value == 'desc':
            assert current_prices == (sorted(
                current_prices))[::-1], 'Сортировка по цене в убывающем порядке выполнена некорректно'
        if value == 'asc':
            assert current_prices == sorted(
                current_prices), 'Сортировка по цене в возрастающем порядке выполнена некорректно'

    @pytest.mark.parametrize('value',
                             TestdataFilter.category_type
                             )
    def test_filter_by_category(self,driver,value):#12
        main_page = MainPage(driver)
        main_page.click_category_dropdown()
        main_page.choose_category(value)
        current_tittle = CardCategoryGetter.collect_all_category_across_pages(driver)
        for i in range(len(current_tittle)):
            flag = main_page.check_category(value,current_tittle[i])
            if not flag:
                assert False, 'В выдаче объявления несоответсвуют выбранной в фильтре категории'

        assert True

    def test_priority_toggle(self,driver):#13
        main_page = MainPage(driver)
        main_page.click_priority_toggle()
        time.sleep(3)
        cards = CardGetter.get_all_cards_from_current_page(driver)


        flag = main_page.verify_all_cards_have_priority(cards)

        assert flag, 'Не все карточки в выдаче имеют приоритет "Срочный"'


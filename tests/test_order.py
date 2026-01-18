import allure
from url import *
from pages.order_page import OrderPage

class TestOrder():
    @allure.title('Проверка увеличения счетчика «Выполнено за всё время» на один при выполнении заказа')
    def test_increase_total_counter(self, driver, logged_in_user):
        order_page = OrderPage(driver)

        current_number = order_page.check_total_counter()

        assert current_number == order_page.initial_count + 1

    @allure.title('Проверка увеличения счетчика «Выполнено за сегодня» на один при выполнении заказа')
    def test_increase_today_counter(self, driver, logged_in_user):
        order_page = OrderPage(driver)

        current_number = order_page.check_day_counter()

        assert current_number == order_page.initial_count + 1

    @allure.title('Проверка появления номера заказа в разделе "В работе" после его оформления')
    def test_number_in_process(self, driver, logged_in_user):
        order_page = OrderPage(driver)

        current_number = order_page.check_in_process()

        assert current_number == order_page.initial_count
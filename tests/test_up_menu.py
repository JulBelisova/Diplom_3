import allure
from url import *
from pages.up_menu_page import UpMenuPage

class TestUpMenu():

    @allure.title('Проверка перехода на страницу Лента заказов по клику на раздел верхнего меню "Лента заказов"')
    def test_feed_button(self, driver):
        up_menu_page = UpMenuPage(driver)
        up_menu_page.click_feed_button()

        current_url = up_menu_page.get_current_url()
        assert current_url == order_page

    @allure.title('Проверка перехода на страницу Конструктора бургеров по клику на раздел верхнего меню "Конструктор"')
    def test_builder_button(self, driver):
        up_menu_page = UpMenuPage(driver)
        up_menu_page.open_feed_page_and_click_builder

        current_url = up_menu_page.get_current_url()
        assert current_url == main_site
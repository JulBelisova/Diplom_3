import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderLocators
from locators.builder_page_locators import BuilderPageLocators
from locators.up_menu_locators import UpMenuLocators
from .base_page import BasePage
from url import *

class OrderPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.initial_count = None   

    @allure.step('Открыть страницу с лентой заказов')
    def open_order_page(self):
        self.click_element(UpMenuLocators.feed_button)

    @allure.step('Подождать открытия ленты заказов')
    def wait_feed_open(self):
        self.find_element(OrderLocators.counter_total)

    @allure.step('Сохранить количество заказов')
    def save_all_orders_number(self):
        text = self.get_text(OrderLocators.counter_total)
        self.initial_count = int(text)
        return self.initial_count

    @allure.step('Открыть страницу с конструктором')
    def open_builder_page(self):
        self.click_element(UpMenuLocators.builder_button)

    @allure.step('Перетаскивание ингредиента в конструктор')
    def move_bun_to_the_builder(self):
        self.drag_and_drop(BuilderPageLocators.bun, BuilderPageLocators.up_bun_builder)

    @allure.step('Кликнуть "Оформить заказ"')
    def click_order_button(self):
        self.click_element(OrderLocators.order_button)    

    @allure.step('Дождаться пока крестик станет кликабельным')
    def wait_for_close_button(self):
        self.find_element_clickable(OrderLocators.close_order_info) 

    @allure.step('Кликнуть на крестик для закрытия информации о заказе')
    def click_close_order_info(self):
        self.click_element(OrderLocators.close_order_info) 

    @allure.step('Получить текущее количество заказов')
    def get_current_orders_number(self):
        text = self.get_text(OrderLocators.counter_total)
        return int(text)
    
    @allure.step('Подождать окончания загрузки')
    def wait_for_cover_to_disappear(self):
        self.wait_until_element_invisible(OrderLocators.cover)

    @allure.step('Подождать загрузки страницы конструктора')
    def wait_for_builder_page(self):
        self.find_element(BuilderPageLocators.build_your_burger)  

    @allure.step('Подождать загрузки страницы ленты заказов')
    def wait_for_feed_page(self):
        self.find_element(UpMenuLocators.name_feed)


    @allure.step('Подождать окончания загрузки')
    def wait_for_cover_infa_to_disappear(self):
        self.wait_until_element_invisible(OrderLocators.cover_order_infa) 

    @allure.step('Оформление заказа и сохранение номера из счетчика')
    def check_total_counter(self):
        self.open_order_page()
        self.wait_feed_open()
        self.save_all_orders_number()
        self.open_builder_page()
        self.move_bun_to_the_builder()
        self.click_order_button()
        self.wait_for_cover_to_disappear()
        self.wait_for_close_button()
        self.click_close_order_info()
        self.wait_for_cover_infa_to_disappear()
        self.wait_for_builder_page()
        self.open_order_page()
        self.wait_for_feed_page()
        self.wait_feed_open()
        element = self.get_current_orders_number()
        return element
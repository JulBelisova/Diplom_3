import allure
from locators.up_menu_locators import UpMenuLocators
from .base_page import BasePage
from url import *

class UpMenuPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликнуть на раздел «Лента заказов»')
    def click_feed_button(self):
        self.click_element(UpMenuLocators.feed_button)
    
    @allure.step('Кликнуть на раздел «Конструктор»')
    def click_builder_button(self):
        self.click_element(UpMenuLocators.builder_button)

    @allure.step('Ожидание появления заголовка "Лента заказов"')
    def wait_for_name(self):
        self.find_element(UpMenuLocators.name_feed)

    @allure.step('Открытие страницы "Лента заказов"')
    def open_feed_page(self):
        self.open_page(order_page)

    @allure.step('Открытие ленты заказов и последующее открытие страницы конструктора')
    def open_feed_page_and_click_builder(self):
        self.open_feed_page()
        self.wait_for_name()
        self.click_builder_button()
    

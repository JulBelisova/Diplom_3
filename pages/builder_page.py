import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.builder_page_locators import BuilderPageLocators
from .base_page import BasePage
from url import *

class BuilderPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликнуть на первую булку')
    def click_first_bun(self):
        self.click_element(BuilderPageLocators.bun)

    @allure.step('Подождать открытия вплывающего окна с деталями заказа')
    def wait_for_order_details(self):
        self.find_element(BuilderPageLocators.ingredient_details)

    @allure.step('Найти название ингредиента во всплывающем окне')
    def look_for_ingredient_name(self):
        return self.get_text(BuilderPageLocators.ingredient_name)

    @allure.step('Открытие вплывающего окна с деталями заказа')
    def open_order_details(self):
        self.click_first_bun()
        self.wait_for_order_details()
        element = self.look_for_ingredient_name()
        return element
    
    @allure.step('Закрытие вплывающего окна с деталями заказа')
    def click_close_button(self):
        self.click_element(BuilderPageLocators.close_button)

    @allure.step('Ожидание загрузки главной страницы')
    def wait_for_name_to_appear(self):
        self.find_element(BuilderPageLocators.build_your_burger)
    
    @allure.step('Появляется заголовок Соберите бургер после закрытия всплывающего окна')
    def name_is_visible(self):
        return self.get_text(BuilderPageLocators.build_your_burger)

    @allure.step('Открытие вслывающего окна с деталями заказа и последующее его закрытие')
    def close_order_details(self):
        self.click_first_bun()
        self.wait_for_order_details()
        self.click_close_button()
        self.wait_for_name_to_appear()
        element = self.name_is_visible()
        return element
    
    @allure.step('Перетаскивание ингредиента в конструктор')
    def move_bun_to_the_builder(self):
        self.drag_and_drop(BuilderPageLocators.bun, BuilderPageLocators.up_bun_builder)

    @allure.step('Проверка увеличения счетчика на два')
    def counter_two(self):
        return self.get_text(BuilderPageLocators.counter)

    @allure.step('Перенос булочки и проверка увеличения счетчика')
    def check_counter(self):
        self.move_bun_to_the_builder()
        number = self.counter_two()
        return number

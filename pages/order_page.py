import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderLocators
from .base_page import BasePage
from url import *

class OrderPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликнуть на кнопку "Личный кабинет"')
    def click_account(self):
        self.click_element(OrderLocators.account_button)

    @allure.step('Кликнуть на кнопку "Зарегистрироваться"')
    def click_sigh_up(self):
        self.click_element(OrderLocators.sign_up_button)
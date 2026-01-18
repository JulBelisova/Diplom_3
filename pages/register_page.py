import allure
from selenium.webdriver.support import expected_conditions as EC
from locators.register_locators import RegisterLocators
from .base_page import BasePage
from url import *

class RegisterPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликнуть на кнопку "Личный кабинет"')
    def click_account(self):
        self.click_element(RegisterLocators.account_button)

    @allure.step('Кликнуть на кнопку "Зарегистрироваться"')
    def click_sigh_up(self):
        self.click_element(RegisterLocators.sign_up_button)

    @allure.step('Заполнить поле имени: {name}')
    def enter_name(self, name):
        """Заполняет поле имени"""
        self.send_keys(RegisterLocators.name, name)
    
    @allure.step('Заполнить поле email: {email}')
    def enter_email(self, email):
        """Заполняет поле email"""
        self.send_keys(RegisterLocators.email, email)
        
    @allure.step('Заполнить поле пароля')
    def enter_password(self, password):
        """Заполняет поле пароля"""
        self.send_keys(RegisterLocators.password, password)

    @allure.step('Нажать кнопку регистрации')
    def click_register_button(self):
        """Нажимает кнопку регистрации"""
        self.click_element(RegisterLocators.to_sign_up)

    @allure.step('Регистрация пользователя')
    def register_user(self, user_data):
        self.click_account()
        self.click_sigh_up()
        self.enter_name(user_data["name"])
        self.enter_email(user_data["email"])
        self.enter_password(user_data["password"])
        self.click_register_button()
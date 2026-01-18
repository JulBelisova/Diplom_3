from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.login_locators import LoginLocators
from locators.builder_page_locators import BuilderPageLocators
from .base_page import BasePage
import allure

class LoginPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    

    @allure.step('Заполнить поле email: {email}')
    def enter_email(self, email):
        self.send_keys(LoginLocators.email, email)
        
    @allure.step('Заполнить поле пароля')
    def enter_password(self, password):
        self.send_keys(LoginLocators.password, password)

    @allure.step('Нажать кнопку войти')
    def click_enter_button(self):
        self.click_element(LoginLocators.sing_in)


    @allure.step('Войти с email: {email} и паролем')
    def login(self, email, password):

        self.enter_email(email)
        self.enter_password(password)
        self.click_enter_button()

        

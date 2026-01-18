from selenium.webdriver.common.by import By


class RegisterLocators:
    account_button = [By.XPATH, ".//p[@class ='AppHeader_header__linkText__3q_va ml-2'][text()='Личный Кабинет']"]
    sign_up_button = [By.XPATH, ".//a[@class = 'Auth_link__1fOlj'][text()='Зарегистрироваться']"]
    name = [By.XPATH, ".//label[text()='Имя']/following-sibling::input"]
    email = [By.XPATH, ".//label[text()='Email']/following-sibling::input"]
    password = [By.XPATH, ".//label[text()='Пароль']/following-sibling::input"]
    to_sign_up = [By.XPATH, ".//button[@class = 'button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"]

from selenium.webdriver.common.by import By


class LoginLocators:
    email = [By.XPATH, ".//label[text()='Email']//following-sibling::input"]
    password = [By.XPATH, ".//label[text()='Пароль']//following-sibling::input"]
    sing_in = [By.XPATH, ".//button[text()='Войти']"]
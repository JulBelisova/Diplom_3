from selenium.webdriver.common.by import By


class UpMenuLocators:
    feed_button = [By.XPATH, ".//p[@class = 'AppHeader_header__linkText__3q_va ml-2'][text() = 'Лента Заказов']"]
    builder_button = [By.XPATH, ".//p[@class = 'AppHeader_header__linkText__3q_va ml-2'][text() = 'Конструктор']"]
    name_feed = [By.XPATH, "//h1[@class ='text text_type_main-large mt-10 mb-5'][text()='Лента заказов']"]


    
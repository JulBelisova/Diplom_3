import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Ожидание появления элемента')
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step('Кликнуть на элемент')
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step('Получить текст элемента')
    def get_text(self, locator):
        return self.find_element(locator).text
    
    @allure.step('Вернуть атрибут элемента')
    def get_attribute(self, locator, attribute):
        return self.find_element(locator).get_attribute(attribute)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ввести текст в поле ввода')
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Подождать до открытия определенного количества окон')
    def wait_until_several_windows_open(self, number):
        return self.wait.until(EC.number_of_windows_to_be(number))

    @allure.step('Переключиться на другое окно')
    def switch_to_another_window(self):
        self.wait_until_several_windows_open(2)
        self.driver.switch_to.window(self.driver.window_handles[-1])
    
    @allure.step('Ожидание, что URL содержит текст')
    def wait_for_url_contains(self, text):
        return self.wait.until(EC.url_contains(text))
    
    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Открыть страницу по URL')
    def open_page(self, url):
        self.driver.get(url)
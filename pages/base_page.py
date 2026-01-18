import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Ожидание появления элемента')
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    @allure.step('Ожидание кликабельности элемента')
    def find_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))
    
    @allure.step('Кликнуть на элемент')
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step('Получить текст элемента')
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Ввести текст в поле ввода')
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)
    
    @allure.step('Ожидание, что URL содержит текст')
    def wait_for_url_contains(self, text):
        return self.wait.until(EC.url_contains(text))
    
    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Открыть страницу по URL')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Подождать до исчезновения окна')
    def wait_until_element_invisible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step('Перетащить элемент {source_locator} на элемент {target_locator}')
    def drag_and_drop(self, source_locator, target_locator):
     
        source_element = self.find_element(source_locator)
        target_element = self.find_element(target_locator)
        
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()
        
        return True
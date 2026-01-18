import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from data import TestDataGenerator

from url import *



@pytest.fixture(params=['chrome', 'firefox'], scope='function')
def driver(request):
    if request.param == 'chrome':
        options = ChromeOptions()
        service = ChromeService()
        browser = webdriver.Chrome(options=options, service=service)
    else:  
        options = FirefoxOptions()
        service = FirefoxService()
        browser = webdriver.Firefox(options=options, service=service)
    
    browser.get(main_site)
    browser.maximize_window()
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def test_user():
    return TestDataGenerator.user_data()

@pytest.fixture(scope="function")
def registered_user(driver, test_user):
    from pages.register_page import RegisterPage
    
    register_page = RegisterPage(driver)
    register_page.register_user(test_user)
    
    return test_user

@pytest.fixture(scope="function")
def logged_in_user(driver, registered_user):
    from pages.login_page import LoginPage
    
    login_page = LoginPage(driver)
    login_page.login(registered_user["email"], registered_user["password"])
    
    return registered_user
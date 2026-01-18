import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

from url import *



@pytest.fixture(params=['chrome', 'firefox'], scope='function')
def driver(request):
    if request.param == 'chrome':
        options = ChromeOptions()
        service = ChromeService()
        browser = webdriver.Chrome(options=options, service=service)
    else:  # firefox
        options = FirefoxOptions()
        service = FirefoxService()
        browser = webdriver.Firefox(options=options, service=service)
    
    browser.get(main_site)
    browser.maximize_window()
    yield browser
    browser.quit()
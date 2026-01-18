from selenium.webdriver.common.by import By


class OrderLocators:
    order_button = [By.XPATH, ".//button[text()='Оформить заказ']"]
    counter_total = [By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p"]
    counter_today = [By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p"]
    close_order_info = [By.XPATH, ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@class= 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
    cover = [By.XPATH, ".//div[@class = 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5']"]
    cover_order_infa = [By.XPATH, ".//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']"]

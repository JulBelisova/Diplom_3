from selenium.webdriver.common.by import By


class BuilderPageLocators:
    bun = [By.XPATH, ".//p[@class = 'BurgerIngredient_ingredient__text__yp3dH'][text()='Флюоресцентная булка R2-D3']"]
    ingredient_details = [By.XPATH, ".//h2[@class = 'Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10'][text()='Детали ингредиента']"]
    ingredient_name = [By.XPATH, ".//p[@class= 'text text_type_main-medium mb-8']"]
    close_button = [By.XPATH, ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']"]
    build_your_burger = [By.XPATH, ".//h1[@class = 'text text_type_main-large mb-5 mt-10'][text()='Соберите бургер']"]
    counter = [By.XPATH, "//p[contains(text(), 'Флюоресцентная булка')]/ancestor::a[contains(@class, 'BurgerIngredient')]//p[contains(@class, 'counter_counter__num')]"]
    up_bun_builder = [By.XPATH, ".//div[@class = 'constructor-element constructor-element_pos_top']//span[@class = 'constructor-element__row']"]
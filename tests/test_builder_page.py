import allure
from url import *
from pages.builder_page import BuilderPage

class TestBuilder():
    @allure.title('Проверка открытия всплывающего окна с деталями об ингредиенте при клике на ингредиент')
    def test_feed_button(self, driver):
        builder_page = BuilderPage(driver)
        ingredient_name = builder_page.open_order_details()

        assert "Флюоресцентная булка R2-D3" in ingredient_name

    @allure.title('Проверка закрытия всплывающего окна кликом по крестику')
    def test_close_button(self, driver):
        builder_page = BuilderPage(driver)
        element = builder_page.close_order_details()
        
        assert element == "Соберите бургер"

    @allure.title('Проверка увеличения счётчика ингредиента при добавлении этого ингредиента в заказ')
    def test_close_button(self, driver):
        builder_page = BuilderPage(driver)
        number = builder_page.check_counter()

        assert number == '2'
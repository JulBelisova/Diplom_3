import allure
import pytest
from data import TestDataGenerator

class TestRegistration:
    
    @allure.title('Проверка регистрации нового пользователя')
    def test_user_registration_and_login(self, driver):
        """
        Тест:
        1. Генерируем данные
        2. Регистрируем пользователя
        3. Проверяем что регистрация прошла успешно
        4. Логинимся с этими данными
        5. Проверяем что вошли успешно
        """
        from pages.register_page import RegisterPage
        from pages.login_page import LoginPage
        
        # 1. Генерируем данные
        user_data = TestDataGenerator.user_data()
        print(f"Тестовые данные: {user_data['email']}")
        
        # 2. Регистрируем
        register_page = RegisterPage(driver)
        register_page.register_user(user_data)
        
        # 3. Проверяем успешность регистрации
        assert register_page.is_registration_successful(), \
            f"Регистрация не удалась для {user_data['email']}"
        
        # 4. Логинимся
        login_page = LoginPage(driver)
        login_page.login(user_data["email"], user_data["password"])
        
        # 5. Проверяем что вошли
        assert login_page.is_user_logged_in(), \
            f"Не удалось войти после регистрации {user_data['email']}"
        
        print(f"✅ Пользователь {user_data['email']} успешно зарегистрирован и вошел")
import random
import string

class TestDataGenerator:
    
    @staticmethod
    def random_string(length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))
    
    @staticmethod  
    def random_email():
        name = TestDataGenerator.random_string(8)  # vasiliy
        domain = TestDataGenerator.random_string(6)  # yandex
        return f"{name}@{domain}.ru"  # vasiliy@yandex.ru
    
    @staticmethod
    def user_data():
        return {
            "name": f"User{random.randint(100, 999)}",  # User123
            "email": TestDataGenerator.random_email(),  # vasiliy@yandex.ru
            "password": f"Pass{random.randint(1000, 9999)}"  # Pass1234
        }
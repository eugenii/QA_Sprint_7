import random
import string

# Метод генерирует строку, состоящую только из букв нижнего регистра
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

# Метод возвращает кортеж с логином, паролем и именем курьера
def register_new_courier_and_return_login_password():
    # Генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # Возвращаем кортеж с данными
    return login, password, first_name
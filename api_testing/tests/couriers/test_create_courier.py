import allure
import pytest

from api_testing.methods.courier_methods import CourierMethods


class TestCourierCreation:
    """Создание курьера."""

    @allure.title('Успешное созлание курьера.')
    @allure.description('Проверка успешного создания курьера.')
    def test_create_courier_success(self, courier_fixture):
        """Проверка успешного создания курьера."""
        login, password, firstname, response = courier_fixture
        
        assert response[0] == 201, "Не удалось создать курьера"
        assert response[1].get("ok") is True, "Неожиданный ответ сервера"

    @allure.title('Попытка создать курьера - с занятыми данными.')
    @allure.description('Проверка ошибки при создании курьера с повторяющимися данными.')
    def test_create_courier_doubled(self, courier_fixture):
        """Проверка успешного создания курьера."""
        login, password, firstname, response = courier_fixture
        courier_methods = CourierMethods()

        # Отправляем запрос на создание курьера с повторяющимися данными
        response_status, response_data = courier_methods.create_courier(login, password, firstname)
        # Проверяем сообщение об ошибке
        actual_message = response_data.get("message")
        expected_message = "Этот логин уже используется. Попробуйте другой."

        assert response_status == 409, f"Ожидался статус 409, но получен {response_status}"
        assert actual_message == expected_message, (
            f"Ожидалось сообщение '{expected_message}', но получено '{actual_message}'"
        )

    @allure.title('Попытки создать курьера с недостаточными данными.')
    @allure.description('Проверка неуспешного создания курьера без логина или без пароля')
    @pytest.mark.parametrize(
        "login, password, firstname, expected_message",
        [
            ("", "", "", "Недостаточно данных для создания учетной записи"),
            ("login", "", "", "Недостаточно данных для создания учетной записи"),
            ("", "password", "", "Недостаточно данных для создания учетной записи"),
            ("", "", "firstname", "Недостаточно данных для создания учетной записи"),
        ]
    )
    def test_create_courier_invalid_data(self, login, password, firstname, expected_message):
        """Проверка неуспешного создания курьера с некорректными данными."""
        # Создаем экземпляр класса CourierMethods
        courier_methods = CourierMethods()

        # Отправляем запрос на создание курьера с некорректными данными
        response_status, response_data = courier_methods.create_courier(login, password, firstname)

        # Проверяем статус ответа
        assert response_status == 400, f"Ожидался статус 400, но получен {response_status}"

        # Проверяем сообщение об ошибке
        actual_message = response_data.get("message")
        assert actual_message == expected_message, (
            f"Ожидалось сообщение '{expected_message}', но получено '{actual_message}'"
        )
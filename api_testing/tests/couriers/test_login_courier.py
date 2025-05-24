import allure
import pytest

from api_testing.methods.courier_methods import CourierMethods
from api_testing.data import test_login, test_login_id
from api_testing.data import COURIERS_URL
from api_testing.helpers.create_user import register_new_courier_and_return_login_password


class TestCourierLogin:
    """Логин курьера."""
    
    @allure.step('Логин курьера - успешный вариант.')
    def test_login_courier_success(self):
        """Проверка успешного логина курьера."""
        # Создаем экземпляр класса CourierMethods
        courier_methods = CourierMethods()
        response = courier_methods.get_courier_id(test_login["login"], test_login["password"])

        assert response == test_login_id["id"], "Получен неверный id"

    @allure.step('Логин курьера - неполные предоставленные данные.')
    @pytest.mark.parametrize(
        "login, password, expected_message",
        [
            (test_login["login"], "", "Недостаточно данных для входа"),
            ("", test_login["password"], "Недостаточно данных для входа")
        ]
    )
    def test_login_few_parameters_returns_error(self, login, password, expected_message):
        """Проверка ошибки при логине с недостаточными данными."""

        courier_methods = CourierMethods()
        response = courier_methods.login_courier(login, password)

        assert response[0] == 400, f"Неверный статус ответа, ожидалось 400, вернулся {response[0]}"
        assert response[1].get("message") == expected_message, f"{response[1].get("message")} != {expected_message  }"

    @allure.step('Попытка логина с несуществующими данными.')
    def test_login_with_not_existent_pair(self):
        """Проверка ошибки при логине с несуществующими данными."""
        login, password, _ = register_new_courier_and_return_login_password()
        expected_message = "Учетная запись не найдена"
        courier_methods = CourierMethods()
        response = courier_methods.login_courier(login*2, password*2)
        print('\n', response[1].get("message"))
        assert response[0] == 404, f"Неверный статус ответа, ожидалось 404, вернулся {response[0]}"
        assert response[1].get("message") == expected_message, f"{response[1].get("message")} != {expected_message}"

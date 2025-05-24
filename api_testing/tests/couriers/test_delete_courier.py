import allure
import pytest

from api_testing.methods.courier_methods import CourierMethods
from api_testing.data import test_login, test_login_id
from api_testing.data import COURIERS_URL
from api_testing.helpers.create_user import register_new_courier_and_return_login_password


class TestCourierDelete:
    """Удаление курьера."""
    
    @allure.title('Успешное удаление курьера.')
    @allure.description('Проверка успешного удаления курьера.')
    def test_delete_courier_success(self, courier_fixture):
        """Проверка удаления курьера по ID."""
        # Создаем экземпляр класса CourierMethods
        login, password, firstname = register_new_courier_and_return_login_password()
        courier_methods = CourierMethods()
        # Создаем курьера.
        response = courier_methods.create_courier(login, password, firstname)
        # Результат создания курьера и его ID.
        creation_result = response[0]
        new_courier_id = courier_methods.get_courier_id(login, password)
        # Удаление курьера по ID.
        result_response = courier_methods.delete_courier(new_courier_id)

        assert result_response[1].get('ok') == True, "Удаление не удалось"


    @allure.title('Не успешное удаление курьера.')
    @allure.description('Проверка попыток удаления курьера без ID или по неправильному ID.')
    @pytest.mark.parametrize(
        "courier_id, status_code, expected_message",
        [
            ("", 404, "Not Found."),
            (-1, 404, "Курьера с таким id нет."),
        ]
    )
    def test_delete_courier_failed(self, courier_id, status_code, expected_message):
        """Проверка удаления курьера по невалидным ID."""
        # Создаем экземпляр класса CourierMethods
        courier_methods = CourierMethods()
        # Удаление курьера по ID.
        response = courier_methods.delete_courier(courier_id)

        assert response[0] == status_code, f"Неверный статус-код ответа. Ожидалось: {status_code}, получено: {response[0]}"
        assert response[1].get("message") == expected_message, f"Неверное сообщение об ошибке. Ожидалось: '{expected_message}', получено: '{response[1].get('message')}'"
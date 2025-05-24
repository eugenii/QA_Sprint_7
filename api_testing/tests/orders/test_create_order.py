import allure
import pytest

from api_testing.methods.order_methods import OrderMethods
from api_testing.data import ORDER_DATA_1, ORDER_DATA_2


class TestOrderCreation:

    @allure.title('Проверка успешного создания заказа разных цветов.')
    @allure.description('Варианты: по 1 цвету, оба цвета, ни одного цвета.')
    @pytest.mark.parametrize(
        "order_data, colors",
        [
            (ORDER_DATA_1, ["BLACK", ""]),
            (ORDER_DATA_2, ["BLACK", "GREY"]),
            (ORDER_DATA_1, ["GREY", ""]),
            (ORDER_DATA_2, ["", ""]),
        ]
    )
    def test_create_order_success(self, order_data, colors):
        """Проверка успешного создания заказа."""
        order_methods = OrderMethods()
        response = order_methods.create_order(order_data, colors)
        
        assert response[0] == 201, "Не удалось создать заказ"
        assert "track" in response[1], "Не удалось получить трек-номер" 
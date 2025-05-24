import allure
import pytest

from api_testing.methods.order_methods import OrderMethods
from api_testing.data import ORDERS_URL


class TestOrderList:

    @allure.title('Проверка наличия списка заказов в теле ответа.')
    @allure.description('Запорос GET без параметров')
    def test_order_list_in_response(self):
        """Проверка наличия списков заказов в ответе."""

        order_methods = OrderMethods()
        response = order_methods.get_order_list(ORDERS_URL)
        
        assert response[0] == 200, "Ответ не получен"
        assert "orders" in response[1], "Поля 'orders' не найдены"  
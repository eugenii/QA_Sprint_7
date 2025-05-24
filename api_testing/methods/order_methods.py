from datetime import datetime, timedelta

import allure
import requests
from api_testing.data import ORDERS_URL


class OrderMethods:
    
    @allure.step('Создаём заказ.')
    def create_order(self, parameters, colors):
        """Создание заказа."""

        # получаем текущую дату
        today = datetime.today()
        # следующий день
        next_day = today + timedelta(days=1)
        # форматируем дату в строку "ГГГГ-ММ-ДД"
        formatted_date = next_day.strftime('%Y-%m-%d')
        parameters['deliveryDate'] = formatted_date
        parameters['color'] = colors
        response = requests.post(
            ORDERS_URL,
            parameters
        )
        return response.status_code, response.json()
    
    @allure.step('Получаем список заказов.')
    def get_order_list(self, parameters):
        """Получение списка заказов."""
        response = requests.get(ORDERS_URL)
        return response.status_code, response.json()
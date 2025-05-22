import requests
from api_testing.data import COURIERS_URL


class CourierMethods:
    
    def create_courier(self, login, password, firstname):
        """Создание курьера."""
        response = requests.post(
            COURIERS_URL,
            json={'login': login, 'password': password, 'firstname': firstname}
        )    
        return response.status_code, response.json()
    
    def delete_courier(self, courier_id):
        """Удаление курьера по его ID."""
        response = requests.delete(
            f"{COURIERS_URL}/{courier_id}"
        )
        return response.status_code
    
    def get_courier_id(self, login, password):
        """Получение ID курьера по логину и паролю."""
        response = requests.post(
            f"{COURIERS_URL}/login",
            json={'login': login, 'password': password}
        )
        if response.status_code == 200:
            return response.json().get('id')
        return None
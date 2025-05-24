BASE_URL = 'https://qa-scooter.praktikum-services.ru/'
ORDERS_URL = BASE_URL + 'api/v1/orders'
COURIERS_URL = BASE_URL + 'api/v1/courier'

ORDER_DATA_1 = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 2,
    "comment": "Saske, come back to Konoha",
}
ORDER_DATA_2 = {
    "firstName": "Naruto2",
    "lastName": "Uchiha2",
    "address": "Konoha, 100 apt.",
    "metroStation": 5,
    "phone": "+7 800 355 35 35",
    "rentTime": 2,
    "comment": "just another order",
}

# https://qa-scooter.praktikum-services.ru/api/v1/courier/

test_login = {
    "login": "ninjaX1r1Z",
    "password": "123456"
}

test_login_id = {
    "id": 527034
}
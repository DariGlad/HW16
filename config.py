from os import path

parent_dir = path.dirname(path.abspath(__file__))
USERS_DATA = path.join(parent_dir, "data", "users.json")  # путь к данным пользователя
ORDERS_DATA = path.join(parent_dir, "data", "orders.json")  # путь к данным заказчика
OFFERS_DATA = path.join(parent_dir, "data", "offers.json")  # путь к данным исполнителей

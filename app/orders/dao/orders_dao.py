import json

from classes.models import Order
from config import ORDERS_DATA
from utils import db


class OrdersDAO:
    """ Класс для работы с базами данных заказчиков """

    def __init__(self, path=ORDERS_DATA):
        self.path = path

    def create_orders(self):
        """ Метод заполняет базу данных заказчиков из json файла"""

        with open(self.path, "r", encoding="UTF-8") as file:
            datas = json.load(file)
            orders = [Order(
                id=data["id"],
                name=data["name"],
                description=data["description"],
                start_date=data["start_date"],
                end_date=data["end_date"],
                address=data["address"],
                price=data["price"],
                customer_id=data["customer_id"],
                executor_id=data["executor_id"]
            ) for data in datas]
            db.session.add_all(orders)
            db.session.commit()

    def new_add(self, order):
        """ Добавляет нового заказчика в базу данных """

        new_order = Order(
            name=order["name"],
            description=order["description"],
            start_date=order["start_date"],
            end_date=order["end_date"],
            address=order["address"],
            price=order["price"],
            customer_id=order["customer_id"],
            executor_id=order["executor_id"]
        )
        db.session.add(new_order)
        db.session.commit()
        return Order.make_dict(new_order)

    def order_update(self, order, new_order):
        """ Обновляет данные заказчика """

        order.name = new_order.get("name")
        order.description = new_order.get("description")
        order.start_date = new_order.get("start_date")
        order.end_date = new_order.get("end_date")
        order.address = new_order.get("address")
        order.price = new_order.get("price")
        order.customer_id = new_order.get("customer_id")
        order.executor_id = new_order.get("executor_id")

        db.session.add(order)
        db.session.commit()
        return Order.make_dict(order)

    def delete_order(self, order):
        """ Удаление данных заказчика """

        db.session.delete(order)
        db.session.commit()

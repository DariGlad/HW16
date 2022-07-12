from flask import Blueprint, request, jsonify
from classes.models import Order
from app.orders.dao.orders_dao import OrdersDAO
from exceptions import IdNotFound

orders_blueprint = Blueprint("orders_blueprint", __name__)


@orders_blueprint.route("/", methods=["GET", "POST"])
def orders_page():
    """
    GET - все данные заказчиков
    POST - добавление данных нового заказчика из полученного json словаря
    """
    if request.method == "GET":
        orders = [Order.make_dict(order) for order in Order.query.all()]
        return jsonify(orders)

    if request.method == "POST":
        data = request.json
        new_order = OrdersDAO().new_add(data)
        return jsonify(new_order)


@orders_blueprint.route("/<int:order_id>/", methods=["GET", "PUT", "DELETE"])
def order_page(order_id):
    """
    GET - возвращает данные заказчика по id,
    PUT - обновляет данные заказчика по id из полученного json словаря,
    DELETE - удаляет данные заказчика
    """
    order = Order.query.get(order_id)  # Ищем заказчика по id
    if order is None:  # Ошибка при отсутствии записи
        raise IdNotFound("Нет такого заказчика")
    if request.method == "GET":
        return jsonify(Order.make_dict(order))
    if request.method == "PUT":
        return jsonify(OrdersDAO().order_update(order, request.json))
    if request.method == "DELETE":
        OrdersDAO().delete_order(order)
        return f" Запись по id {order_id} была удалена"

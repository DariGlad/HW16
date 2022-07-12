from flask import Blueprint, request, jsonify
from classes.models import Offer
from app.offers.dao.offers_dao import OffersDAO
from exceptions import IdNotFound

offers_blueprint = Blueprint("offers_blueprint", __name__)


@offers_blueprint.route("/", methods=["GET", "POST"])
def offers_page():
    """
    GET - все данные исполнителей
    POST - добавление данных нового исполнителя из полученного json словаря
    """

    if request.method == "GET":
        offers = [Offer.make_dict(offer) for offer in Offer.query.all()]
        return jsonify(offers)

    if request.method == "POST":
        data = request.json
        new_offer = OffersDAO().new_add(data)
        return jsonify(new_offer)


@offers_blueprint.route("/<int:offer_id>/", methods=["GET", "PUT", "DELETE"])
def offer_page(offer_id):
    """
    GET - возвращает данные исполнителя по id,
    PUT - обновляет данные исполнителя по id из полученного json словаря,
    DELETE - удаляет данные исполнителя
    """

    offer = Offer.query.get(offer_id)  # Ищем исполнителя по id
    if offer is None:  # Ошибка при отсутствии записи
        raise IdNotFound("Нет такого исполнителя")
    if request.method == "GET":
        return jsonify(Offer.make_dict(offer))
    if request.method == "PUT":
        return jsonify(OffersDAO().offer_update(offer, request.json))
    if request.method == "DELETE":
        OffersDAO().delete_offer(offer)
        return f" Запись по id {offer_id} была удалена"

import json

from classes.models import Offer
from config import OFFERS_DATA
from utils import db


class OffersDAO:
    """ Класс для работы с базами данных исполнителей"""

    def __init__(self, path=OFFERS_DATA):
        self.path = path

    def create_offers(self):
        """ Метод заполняет базу данных исполнителей из json файла"""

        with open(self.path, "r", encoding="UTF-8") as file:
            datas = json.load(file)
            offers = [Offer(
                id=data["id"],
                order_id=data["order_id"],
                executor_id=data["executor_id"]
            ) for data in datas]
            db.session.add_all(offers)
            db.session.commit()

    def new_add(self, offer):
        """ Добавляет нового исполнителя в базу данных """

        new_offer = Offer(
            order_id=offer["order_id"],
            executor_id=offer["executor_id"],
        )
        db.session.add(new_offer)
        db.session.commit()
        return Offer.make_dict(new_offer)

    def offer_update(self, offer, new_offer):
        """ Обновляет данные исполнителя """

        offer.first_name = new_offer.get("order_id")
        offer.last_name = new_offer.get("executor_id")

        db.session.add(offer)
        db.session.commit()
        return Offer.make_dict(offer)

    def delete_offer(self, offer):
        """ Удаление данных исполнителя """

        db.session.delete(offer)
        db.session.commit()

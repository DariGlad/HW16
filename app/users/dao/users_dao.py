import json

from classes.models import User
from config import USERS_DATA
from utils import db


class UsersDAO:
    """ Класс для работы с базами данных пользователей """

    def __init__(self, path=USERS_DATA):
        self.path = path

    def create_users(self):
        """ Метод заполняет базу данных пользователей из json файла"""

        with open(self.path, "r", encoding="UTF-8") as file:
            datas = json.load(file)
            users = [User(
                id=data["id"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                age=data["age"],
                email=data["email"],
                role=data["role"],
                phone=data["phone"]
            ) for data in datas]
            db.session.add_all(users)
            db.session.commit()

    def new_add(self, user):
        """ Добавляет нового пользователя в базу данных """

        new_user = User(
            first_name=user["first_name"],
            last_name=user["last_name"],
            age=user["age"],
            email=user["email"],
            role=user["role"],
            phone=user["phone"]
        )
        db.session.add(new_user)
        db.session.commit()
        return User.make_dict(new_user)

    def user_update(self, user, new_user):
        """ Обновляет данные пользователя """

        user.first_name = new_user.get("first_name")
        user.last_name = new_user.get("last_name")
        user.age = new_user.get("age")
        user.email = new_user.get("email")
        user.role = new_user.get("role")
        user.phone = new_user.get("phone")

        db.session.add(user)
        db.session.commit()
        return User.make_dict(user)

    def delete_user(self, user):
        """ Удаление данных пользователя """

        db.session.delete(user)
        db.session.commit()

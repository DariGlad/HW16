from flask import Blueprint, request, jsonify
from classes.models import User
from app.users.dao.users_dao import UsersDAO
from exceptions import IdNotFound

users_blueprint = Blueprint("users_blueprint", __name__)


@users_blueprint.route("/", methods=["GET", "POST"])
def users_page():
    """
    GET - все данные пользователей
    POST - добавление данных нового пользователя из полученного json словаря
    """
    if request.method == "GET":
        users = [User.make_dict(user) for user in User.query.all()]
        return jsonify(users)

    if request.method == "POST":
        data = request.json
        new_user = UsersDAO().new_add(data)
        return jsonify(new_user)


@users_blueprint.route("/<int:user_id>/", methods=["GET", "PUT", "DELETE"])
def user_page(user_id):
    """
    GET - возвращает данные пользователя по id,
    PUT - обновляет данные пользователя по id из полученного json словаря,
    DELETE - удаляет данные пользователя
    """
    user = User.query.get(user_id)  # Ищем пользователя по id
    if user is None:  # Ошибка при отсутствии записи
        raise IdNotFound("Нет такого пользователя")
    if request.method == "GET":
        return jsonify(User.make_dict(user))
    if request.method == "PUT":
        return jsonify(UsersDAO().user_update(user, request.json))
    if request.method == "DELETE":
        UsersDAO().delete_user(user)
        return f" Запись по id {user_id} была удалена"

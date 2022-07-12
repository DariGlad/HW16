from flask import Blueprint

from exceptions import IdNotFound

errors_blueprint = Blueprint("errors_blueprint", __name__)


@errors_blueprint.app_errorhandler(IdNotFound)  # Обработчик ошибки при отсутствии id
def errors_id_not_found(e):
    return f"<center><h1>{e}</h1></center>"

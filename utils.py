from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def app_create():
    """ Функция создания экземпляра класса Flask с настройками базы данных """

    app = Flask(__name__)
    app.config["JSON_AS_ASCII"] = False  # отключаем кодировку ASCII для отображения кириллицы
    app.config["JSON_SORT_KEYS"] = False  # отключаем сортировку ключей JSON
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # подключение к базе данных
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True  # Для построчного отображения ключей в формате json в браузере

    db.init_app(app)  # связываем экземпляры классов базы данных и Flask
    app.app_context().push()  # связываю контексты приложений
    return app

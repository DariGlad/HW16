from app.errors.views import errors_blueprint
from app.offers.dao.offers_dao import OffersDAO
from app.offers.views import offers_blueprint
from app.orders.dao.orders_dao import OrdersDAO
from app.orders.views import orders_blueprint
from app.users.dao.users_dao import UsersDAO
from app.users.views import users_blueprint
from utils import db, app_create

app = app_create()  # Создаём app и связь bd через функцию
db.create_all()  # Создаём пустые таблицы
UsersDAO().create_users()  # Заполняем таблицу пользователей
OrdersDAO().create_orders()  # Заполняем таблицу заказчиков
OffersDAO().create_offers()  # Заполняем таблицу исполнителей

app.register_blueprint(users_blueprint, url_prefix="/users/")  # Регистрируем блюпринт пользователя
app.register_blueprint(orders_blueprint, url_prefix="/orders/")  # Регистрируем блюпринт заказчика
app.register_blueprint(offers_blueprint, url_prefix="/offers/")  # Регистрируем блюпринт исполнителя
app.register_blueprint(errors_blueprint)  # Регистрируем блюпринт ошибок


@app.route("/")
def main_page():
    return "<center><h1>Привет</h1></center>"


if __name__ == "__main__":
    app.run()

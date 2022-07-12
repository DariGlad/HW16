from utils import db


class User(db.Model):
    """ Класс базы данных пользователей """

    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    email = db.Column(db.String(200))
    role = db.Column(db.String(50))
    phone = db.Column(db.String(50))

    def make_dict(self):
        """ Возвращает данные пользователя в виде словаря """
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "role": self.role,
            "phone": self.phone
        }


class Order(db.Model):
    """ Класс базы данных заказчиков """

    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(200))
    start_date = db.Column(db.String(50))
    end_date = db.Column(db.String(50))
    address = db.Column(db.String(200))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("offer.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def make_dict(self):
        """ Возвращает данные заказчика в виде словаря """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "address": self.address,
            "price": self.price,
            "customer_id": self.customer_id,
            "executor_id": self.executor_id
        }


class Offer(db.Model):
    """ Класс базы данных исполнителя """

    __tablename__ = "offer"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def make_dict(self):
        """ Возвращает данные исполнителя в виде словаря """
        return {
            "id": self.id,
            "order_id": self.order_id,
            "executor_id": self.executor_id,
        }

# пользователи нашего сайта
import datetime

import sqlalchemy
import sqlalchemy.orm as orm
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase

# роль пользователя
ACCESS = {
    'user': 1,
    'admin': 2
}


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    about = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True,
                              unique=True, nullable=True)
    #level = sqlalchemy.Column(sqlalchemy.Integer, default=1)
    hashed_password = sqlalchemy.Column(sqlalchemy.String,
                                        nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                     default=datetime.datetime.now())
    news = orm.relationship("News", back_populates='user')

    def __repr__(self):
        return f'<Объект user, пользователь {self.name}>'

    def __str__(self):
        return f'<Объект user, пользователь {self.name}>'

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

def get_id(self):
    return self.id

#def is_admin(self):
   # return self.level == ACCESS['admin']

#def allowed(self, access_level):
  #  return self.level >= access_level
import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class SavedRecipe(SqlAlchemyBase, SerializerMixin, UserMixin):    #для каждого пользователя есть его сохраненные рецепты
    __tablename__ = 'savedRecipe'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    spoonacular_id = sqlalchemy.Column(sqlalchemy.Integer)
    title = sqlalchemy.Column(sqlalchemy.String)
    image_url = sqlalchemy.Column(sqlalchemy.String)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    saved_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.utcnow)

    recipe_of_user = orm.relationship('User')

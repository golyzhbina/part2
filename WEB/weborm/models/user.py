import sqlalchemy as sa
from .db_session import SqlAlcBase
import datetime
from sqlalchemy import orm


class User(SqlAlcBase):

    __tablename__ = "users"
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    about = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, unique=True)
    hashed_password = sa.Column(sa.String)
    create_date = sa.Column(sa.DateTime, default=datetime.datetime.now)
    news = orm.relation("News", back_populates="user")


from sqlalchemy import Column, Integer, Numeric, Float
from .db_session import SqlAlcBase


class Order(SqlAlcBase):
    __tablename__ = 'order'

    id_ord = Column(Integer, primary_key=True)
    title = Column(Numeric)
    price = Column(Float)
    description = Column(Numeric)

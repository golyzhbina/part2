from sqlalchemy import Column, Integer, Numeric, Float
from .db_session import SqlAlcBase


class Position(SqlAlcBase):
    __tablename__ = 'position'

    id_pos = Column(Integer, primary_key=True)
    name = Column(Numeric)
    description = Column(Numeric)
    oklad = Column(Float)

from sqlalchemy import Column, Integer, String
from .db_session import SqlAlcBase


class Client(SqlAlcBase):
    __tablename__ = 'client'

    id_emp = Column(Integer, primary_key=True)
    surname = Column(String)
    name = Column(String)
    last_name = Column(String)
    phone = Column(String)
    email = Column(String)

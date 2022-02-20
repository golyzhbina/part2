from sqlalchemy import Column, Integer, String
from .db_session import SqlAlcBase


class Employer(SqlAlcBase):
    __tablename__ = 'employer'

    id_emp = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, unique=True)
    email = Column(String, unique=True)
    login = Column(String, unique=True)
    password = Column(String)

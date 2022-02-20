from sqlalchemy import Column, Integer, Numeric, Float, ForeignKey
from sqlalchemy.orm import relationship

from .db_session import SqlAlcBase


class CliOrd(SqlAlcBase):
    __tablename__ = 'cli_ord'

    id_note = Column(Integer, primary_key=True)
    id_cli = Column(ForeignKey('client.id_emp'))
    id_ord = Column(ForeignKey('order.id_ord'))

    client = relationship('Client')
    order = relationship('Order')

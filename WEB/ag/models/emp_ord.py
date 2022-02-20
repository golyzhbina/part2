from sqlalchemy import Column, Integer, Numeric, Float, ForeignKey
from sqlalchemy.orm import relationship

from .db_session import SqlAlcBase


class EmpOrd(SqlAlcBase):
    __tablename__ = 'emp_ord'

    id_note = Column(Integer, primary_key=True)
    id_emp = Column(ForeignKey('employer.id_emp'))
    id_ord = Column(ForeignKey('order.id_ord'))

    employer = relationship('Employer')
    order = relationship('Order')

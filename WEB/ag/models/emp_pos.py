from sqlalchemy import Column, Integer, Numeric, Float, ForeignKey
from sqlalchemy.orm import relationship

from .db_session import SqlAlcBase


class EmpPo(SqlAlcBase):
    __tablename__ = 'emp_pos'

    id_note = Column(Integer, primary_key=True)
    id_emp = Column(ForeignKey('employer.id_emp'))
    id_pos = Column(ForeignKey('position.id_pos'))

    employer = relationship('Employer')
    position = relationship('Position')

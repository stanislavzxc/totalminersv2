from typing import Optional
from sqlalchemy import Column, Integer, String

from ..base_model import Model

class Business(Model):
    __tablename__ = 'business'

    id = Column(Integer, primary_key=True, autoincrement=True)
    miner1 = Column(String, nullable=True)
    count1 = Column(Integer, nullable=True)
    hosting_discount1 = Column(Integer, nullable=True)
    cost1 = Column(Integer, nullable=True)
    miner2 = Column(String, nullable=True)
    count2 = Column(Integer, nullable=True)
    hosting_discount2 = Column(Integer, nullable=True)
    cost2 = Column(Integer, nullable=True)
    miner3 = Column(String, nullable=True)
    count3 = Column(Integer, nullable=True)
    hosting_discount3 = Column(Integer, nullable=True)
    cost3 = Column(Integer, nullable=True)

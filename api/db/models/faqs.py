from typing import Optional
from sqlalchemy import Column, Integer, String

from ..base_model import Model

class Faq(Model):
    __tablename__ = 'faq'

    id = Column(Integer, primary_key=True, autoincrement=True)
    vopros1 = Column(String, nullable=True)
    otvet1 = Column(String, nullable=True)
    vopros2 = Column(String, nullable=True)
    otvet2 = Column(String, nullable=True)
    vopros3 = Column(String, nullable=True)
    otvet3 = Column(String, nullable=True)
   

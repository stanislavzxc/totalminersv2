from typing import Optional
from sqlalchemy import Column, String, Integer

from ..base_model import Model

class Info(Model):
    __tablename__ = 'info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String, nullable=True)
    telegram = Column(String, nullable=True)
    whatsapp = Column(String, nullable=True)
    tiktok = Column(String, nullable=True)
    insta = Column(String, nullable=True)
    copywrite = Column(String, nullable=True)
    

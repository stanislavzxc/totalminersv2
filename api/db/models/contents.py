from typing import Optional
from sqlalchemy import Column, Boolean, Integer

from ..base_model import Model

class Content(Model):
    __tablename__ = 'content'

    id = Column(Integer, primary_key=True, autoincrement=True)
    top20 = Column(Boolean, nullable=True)
    market = Column(Boolean, nullable=True)
    center_info = Column(Boolean, nullable=True)
    tech = Column(Boolean, nullable=True)
    business = Column(Boolean, nullable=True)
    stat = Column(Boolean, nullable=True)
    dashboard = Column(Boolean, nullable=True)
    payments = Column(Boolean, nullable=True)
    miners = Column(Boolean, nullable=True)
    test = Column(Boolean, nullable=True)
    reg = Column(Boolean, nullable=True)
    

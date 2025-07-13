import datetime

from sqlalchemy import ForeignKey, Column, String, Integer, DateTime, BigInteger, Text
from sqlalchemy.orm import relationship

from ..base_model import Model


class News(Model):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'), nullable=True)
    user = relationship('User', foreign_keys=[user_id], uselist=False, lazy='selectin')
    title = Column(String(500), nullable=False)
    description = Column(Text, nullable=False)
    url = Column(String(2048), nullable=False)
    image = Column(Text)
    created = Column(DateTime, default=datetime.datetime.utcnow)

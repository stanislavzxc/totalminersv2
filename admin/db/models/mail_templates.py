import datetime

from sqlalchemy import ForeignKey, Column, String, Integer, DateTime, BigInteger, Text
from sqlalchemy.orm import relationship

from ..base_model import Model


class MailTemplate(Model):
    __tablename__ = 'mail_templates'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(500), nullable=False)
    content = Column(Text, nullable=False)

    mail_campaigns = relationship("MailCampaign", back_populates="template")

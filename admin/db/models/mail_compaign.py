import datetime

from sqlalchemy import ForeignKey, Column, String, Integer, DateTime, BigInteger, Text, Boolean
from sqlalchemy.orm import relationship

from ..base_model import Model


class MailCampaign(Model):
    __tablename__ = 'mail_campaigns'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    template_id = Column(Integer, ForeignKey('mail_templates.id'), nullable=False)
    sent_at = Column(DateTime, default=datetime.datetime.now)
    status = Column(Boolean, default=False)
    
    user = relationship("User", back_populates="mail_campaigns")
    template = relationship("MailTemplate", back_populates="mail_campaigns")

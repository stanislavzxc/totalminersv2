import datetime

from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from ..base_model import Model


class Testmode(Model):
    __tablename__ = 'testmode'
    
    TOTAL_TEST_MODE_HOURS = 72

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='SET NULL'))
    user = relationship('User', foreign_keys=user_id, uselist=False, lazy='selectin')
    state = Column(String, default='active')
    testmodetype = Column(String, default='')
    cost = Column(String, default='')
    hashrate = Column(String, default='')
    hosting = Column(String, default='')
    profit = Column(String, default='')
    created_at = Column(DateTime, default=datetime.datetime.now)
    expires_at = Column(DateTime)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.expires_at:
            self.expires_at = datetime.datetime.utcnow() + datetime.timedelta(hours=self.TOTAL_TEST_MODE_HOURS)

    @property
    def time_left(self):
        now = datetime.datetime.utcnow()
        if now >= self.expires_at:
            return "0ч 0м"
        remaining = self.expires_at - now
        total_seconds = int(remaining.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes = remainder // 60
        return f"{hours}ч {minutes}м"

    @property
    def time_left_seconds(self):
        return max(int((self.expires_at - datetime.datetime.utcnow()).total_seconds()), 0)

from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserRegister(BaseModel):
    email: EmailStr
    password: str
    firstname: str
    lastname: str
    phone: str


class UserVerifyTotp(BaseModel):
    email: EmailStr
    otp: str


class CountryAdd(BaseModel):
    name: str
    short_code: str


class WorkerResponse(BaseModel):
    id: int
    item_name: str
    hosting_cost: str
    profit: str
    dohod: str
    rashod: str
    status: str

class MinerData(BaseModel):
    miner1: str 
    count1: int
    hosting_discount1: int
    сost1: int

    miner2: str
    count2: int
    hosting_discount2: int
    сost2: int

    miner3: str
    count3: int
    hosting_discount3: int
    сost3: int

class ContentData(BaseModel):
    top20: bool
    market: bool
    center_info:  bool
    tech: bool
    business: bool
    stat: bool
    dashboard: bool
    payments: bool
    miners: bool
    test: bool
    reg: bool
    
class FaqData(BaseModel):
    vopros1: str
    otvet1: str
    vopros2: str
    otvet2: str
    vopros3: str
    otvet3: str

class InfoData(BaseModel):
    number: str
    telegram: str
    whatsapp: str
    tiktok: str
    insta: str
    otvecopywritet3: str

class TestmodeData(BaseModel):
    id: int
    user_id: int
    state: str
    testmodetype: str
    cost: str
    hashrate: str
    hosting: str
    profit: str
    created_at: datetime
    expires_at: datetime
    time_left: str  # Форматированная строка "XXч YYм"
    time_left_seconds: int  # Оставшееся время в секундах

    class Config:
        from_attributes = True  # Для совместимости с ORM (ранее alias='orm_mode')




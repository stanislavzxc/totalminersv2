from fastapi import APIRouter, Depends
from api.schemas import MinerData
from api.db.database import get_db
from api.services.business import BusinessService

router = APIRouter(
    prefix='/business',
)


@router.post(path='')
async def update(new_business: MinerData):
    return await BusinessService().add_business_data(new_business)
@router.get(path='')
async def getData():
    return await BusinessService().get_all_business()

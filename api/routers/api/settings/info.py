from fastapi import APIRouter, Depends
from api.schemas import InfoData
from api.services.info import InfoService

router = APIRouter(
    prefix='/info',
)


@router.post(path='')
async def update(new_info: InfoData):
    return await InfoService().add_info(new_info)
@router.get(path='')
async def getData():
    return await InfoService().get_info()

from fastapi import APIRouter, Depends
from api.db.models.testmode import Testmode
from api.services.testmode import TestModeService
from api.schemas import TestmodeData
from pydantic import BaseModel
from api.utils import get_current_user
import datetime

router = APIRouter(
    prefix='/testmode',
)


        
@router.post(path='')
async def create(newtestmode: TestmodeData, user=Depends(get_current_user)):
    data = newtestmode.dict(exclude_unset=True)
    return await TestModeService().create(data, user)

# @router.get(path='')
# async def getData():
#     return await BusinessService().get_all_business()

from fastapi import APIRouter, Depends

from api.services.testmode import TestModeService
from api.utils import get_current_user

router = APIRouter(
    prefix='/get/all',
)


@router.get('')
async def route(user=Depends(get_current_user)):
    result = await TestModeService().get_all(user=user)
    return result

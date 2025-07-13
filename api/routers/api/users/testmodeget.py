from fastapi import APIRouter, Depends
from pydantic import BaseModel

from api.services.testmode import TestModeService
from api.utils import get_current_user

router = APIRouter(
    prefix='/testmode/get',
)


class TestModeGetSchema(BaseModel):
    id: int


@router.get('')
async def route(schema: TestModeGetSchema = Depends(), user=Depends(get_current_user)):
    result = await TestModeService().get(
        user=user,
        id=schema.id,
    )
    return result

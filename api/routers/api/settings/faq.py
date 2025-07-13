from fastapi import APIRouter, Depends
from api.schemas import FaqData
from api.services.faq import FaqService

router = APIRouter(
    prefix='/faq',
)


@router.post(path='')
async def update(new_faq: FaqData):
    return await FaqService().add_faq(new_faq)
@router.get(path='')
async def getData():
    return await FaqService().get_faq()

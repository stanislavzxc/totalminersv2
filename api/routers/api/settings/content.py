from fastapi import APIRouter
from api.services.content import ContentService
from api.schemas import ContentData
router = APIRouter(
    prefix='/content',
)


@router.post(path='')
async def update(content: ContentData):
    return await ContentService().add_content(content)
@router.get(path='')
async def getData():
    return await ContentService().get_all_content()

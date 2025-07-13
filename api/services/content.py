from api.db.models import Content
from api.schemas import ContentData
from api.services.base import BaseService

class ContentService:
    model = Content

    async def get_all_content(self):
        return await BaseService().get_all(self.model)

    async def add_content(self, content: ContentData) -> dict:
        await BaseService().create(
            self.model,
            **content.dict()
        )
        return {
            'result': True,
        }

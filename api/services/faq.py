from api.db.models import Faq
from api.schemas import FaqData
from api.services.base import BaseService

class FaqService:
    model = Faq

    async def get_faq(self):
        return await BaseService().get_all(self.model)

    async def add_faq(self, new_faq: FaqData) -> dict:
        await BaseService().create(
            self.model,
            **new_faq.dict()
        )
        return {
            'result': True,
        }

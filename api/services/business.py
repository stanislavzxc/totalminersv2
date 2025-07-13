from api.db.models import Business
from api.schemas import MinerData
from api.services.base import BaseService

class BusinessService:
    model = Business

    async def get_all_business(self):
        return await BaseService().get_all(self.model)

    async def add_business_data(self, new_business: MinerData) -> dict:
        await BaseService().create(
            self.model,
            **new_business.dict()
        )
        return {
            'result': True,
        }

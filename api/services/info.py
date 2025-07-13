from api.db.models import Info
from api.schemas import InfoData
from api.services.base import BaseService

class InfoServise:
    model = Info

    async def get_info(self):
        return await BaseService().get_all(self.model)

    async def add_info(self, new_info: InfoData) -> dict:
        await BaseService().create(
            self.model,
            **new_info.dict()
        )
        return {
            'result': True,
        }

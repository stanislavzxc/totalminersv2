from api.db.models import User, Testmode
from api.services.base import BaseService
from api.services.user import UserService
from config import settings


class TestModeService:
    model = Testmode

    async def create(self,data: dict,user: User) -> dict:
        data['user_id'] = user.id
        data['user'] = user
        data['state'] = 'wait'
        data['testmodetype'] = 'testmode'
        data['cost'] = '80'
        
        ticket = await BaseService().create(self.model, **data)

        return {
            'status': 'ok',
            'ticket': await self.generate_ticket_dict(ticket=ticket),
        }

    async def get(self, user: User, id: int):
        ticket = await BaseService().get(self.model, user_id=user.id, id=id)
        if not ticket:
            return {
                'status': 'error',
                'description': f'Ticket #{id} not found'
            }
        return {
            'status': 'ok',
            'ticket': await self.generate_ticket_dict(ticket=ticket),
        }

    async def get_all(self, user: User):
        return {
            'status': 'ok',
            'tickets': [
                await self.generate_ticket_dict(ticket=ticket)
                for ticket in await BaseService().get_all(self.model, user_id=user.id)
            ],
        }

    async def close(self, user: User, id: int) -> dict:
        ticket = await BaseService().get(self.model, user_id=user.id, id=id)
        if not ticket:
            return {
                'status': 'error',
                'description': f'Ticket #{id} not found'
            }
        await BaseService().update(ticket, state='stopped')
        return {
            'status': 'ok',
            'ticket': await self.generate_ticket_dict(ticket=ticket),
        }

    @staticmethod
    async def generate_ticket_dict(ticket: Testmode) -> dict:
        if not ticket:
            return {}
        return {
            'id': ticket.id,
            'user': await UserService().generate_user_dict(user=ticket.user),
            'state': ticket.state,
            'testmodetype': ticket.testmodetype,
            'cost': ticket.cost,
            'hashrate': ticket.hashrate,
            'profit': ticket.profit,
            'profit': ticket.profit,
            'date': ticket.created_at.strftime('%d.%m.%Y'),
            'time_left': ticket.time_left,
            'created': ticket.created_at.strftime(format=settings.date_time_format),
        }

    # async def sort_by_status(self, user: User, status: bool):
    #     return {
    #         'status': 'ok',
    #         'ticket': [
    #             await self.generate_ticket_dict(ticket=ticket)
    #             for ticket in await BaseService().get_all(self.model, user_id=user.id, is_open=status)
    #         ]
    #     }
    
    # async def sort_by_date(self, user: User, created_at: datetime):
    #     return {
    #         'status': 'ok',
    #         'ticket': [
    #             await self.generate_ticket_dict(ticket=ticket)
    #             for ticket in await BaseService().get_all(self.model, user_id=user.id, created_at=created_at)
    #         ]
    #     }
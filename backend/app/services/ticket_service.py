
from fastapi.background import P
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.models import Ticket

class TicketService:
    async def get_tickets(self, session: AsyncSession):
        ticket_db = await session.exec(select(Ticket))
        result = ticket_db.all()
        return result
    
    async def purchase_ticket(self):
        pass

    async def get_ticket_by_Id(self):
        pass




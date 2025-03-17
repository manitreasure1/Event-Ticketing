
from fastapi.background import P
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.models import Ticket
from app.db.schemas import PurchaseTicket


class TicketService:
    async def get_tickets(self, session: AsyncSession):
        ticket_db = await session.exec(select(Ticket))
        result = ticket_db.all()
        return result
    
    async def purchase_ticket(self, ticket: PurchaseTicket):
        return ticket

    async def generate_ticket(self):
        pass

    async def send_ticket_to_client(self):
        pass





from typing import Any
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.models import Ticket
from app.db.schemas import PurchaseTicket
from app.db.models import EventAttendance, Ticket

class TicketService:
    async def get_tickets(self, session: AsyncSession):
        ticket_db = await session.exec(select(Ticket))
        result = ticket_db.all()
        return result
    
    async def purchase_ticket(self, ticket: PurchaseTicket, session: AsyncSession, current_user:Any):
        event_attendee = EventAttendance(
            user_id=current_user.id,
            event_id=ticket.event_id
        )
        user_tick = Ticket(
            user_id=current_user.id,
            event_id=ticket.event_id
        )
        # todo : verify account & make deficit from the buyers account
        session.add(event_attendee)
        session.add(user_tick)
        await session.commit()
        await session.refresh(event_attendee)
        await session.refresh(user_tick)
        

    async def generate_ticket(self):
        pass

    async def send_client_ticket(self):
        pass




from fastapi import APIRouter, Depends, Form
from app.services.ticket_service import TicketService
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.sessions import get_session
from typing import Annotated
from app.db.schemas import PurchaseTicket
import logging
from ..dependencies import get_current_user


router = APIRouter()
ticketservice= TicketService()


@router.get("/")
async def get_tickets():
    pass

@router.post("/purchase/")
async def purchase_ticket(*,
                     ticket_data: Annotated[PurchaseTicket, Form()],
                     current_user =Depends(get_current_user),
                     session: AsyncSession = Depends(get_session)
                    ):
    print(ticket_data)
    try:
        await ticketservice.purchase_ticket(
            ticket=ticket_data,
            current_user=current_user,
            session=session
            )
        return {"msg": "ticket purchase successfully"}
    except Exception as e:
        logging.exception(e)
    

@router.get("/{ticket_id}/download/")
def generate_ticket_qrcode():
    pass

@router.post("/{ticket_id}/validate")
def verify_ticket_qrcode():
    pass



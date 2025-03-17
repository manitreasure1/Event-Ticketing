from fastapi import APIRouter, Depends, Form
from app.services.ticket_service import TicketService
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.sessions import get_session
from typing import Annotated, Any
from app.db.schemas import PurchaseTicket
import logging

router = APIRouter()
ticketservice= TicketService()


@router.get("/")
async def get_tickets():
    pass


@router.post("/purchase/")
def purchase_ticket(*, ticket_data: PurchaseTicket):
    print(ticket_data)
    return ticket_data
    
    

@router.get("/{ticket_id}/")
def get_ticket_details():
    pass

@router.get("/{ticket_id}/download/")
def generate_ticket_qrcode():
    pass

@router.post("/{ticket_id}/validate")
def verify_ticket_qrcode():
    pass



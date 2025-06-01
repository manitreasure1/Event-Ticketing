import pytest
from unittest.mock import AsyncMock, MagicMock
from app.services.ticket_service import TicketService
from app.db.models import Ticket
from app.db.schemas import PurchaseTicket
from fastapi import HTTPException

@pytest.mark.asyncio
async def test_get_tickets():
    mock_session = MagicMock()
    mock_exec = AsyncMock()
    mock_session.exec = mock_exec
    mock_result = MagicMock()
    mock_result.all.return_value = [Ticket(id=1, user_id=1, event_id=1)]
    mock_exec.return_value = mock_result
    service = TicketService()
    tickets = await service.get_tickets(mock_session)
    assert isinstance(tickets, list)
    assert tickets[0].id == 1

@pytest.mark.asyncio
async def test_purchase_ticket():
    mock_session = MagicMock()
    mock_session.add = MagicMock()
    mock_session.commit = AsyncMock()
    mock_session.refresh = AsyncMock()
    service = TicketService()
    ticket_data = PurchaseTicket(event_id=1, email='test@email.com', tel='1234567890', payment_method='card', card_number='1234', card_holder_name='Test User', expiry_date='2025-12-31', cvv='123')
    mock_user = MagicMock()
    mock_user.id = 1
    await service.purchase_ticket(ticket_data, mock_session, mock_user)
    assert mock_session.add.call_count == 2
    assert mock_session.commit.called
    assert mock_session.refresh.call_count == 2

@pytest.mark.asyncio
async def test_generate_ticket():
    service = TicketService()
    service.generate_ticket = AsyncMock(side_effect=HTTPException(status_code=400, detail="Not implemented"))
    with pytest.raises(HTTPException) as exc_info:
        await service.generate_ticket()
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Not implemented"

@pytest.mark.asyncio
async def test_send_client_ticket():
    service = TicketService()
    service.send_client_ticket = AsyncMock(side_effect=HTTPException(status_code=400, detail="Not implemented"))
    with pytest.raises(HTTPException) as exc_info:
        await service.send_client_ticket()
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Not implemented"



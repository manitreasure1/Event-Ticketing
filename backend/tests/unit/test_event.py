import pytest
from unittest.mock import AsyncMock, MagicMock
from app.services.event_service import EventService
from app.db.models import Event, EventAttendance, Organization
from app.db.schemas import EventCreate
from fastapi import status
import datetime


@pytest.mark.asyncio
async def test_get_events(session):
    mock_session = MagicMock()
    mock_exec = AsyncMock()
    mock_session.exec = mock_exec
    mock_result = MagicMock()
    mock_result.all.return_value = [Event(id=1, name='Test Event', description='desc', ticket_price=10.0, tickets_available=100, start_date=datetime.datetime.now(), end_data=datetime.datetime.now(), organization_id=1)]
    mock_exec.return_value = mock_result
    service = EventService()
    result = await service.get_events(mock_session)
    assert isinstance(result, list)
    assert result[0].name == 'Test Event'

@pytest.mark.asyncio
async def test_get_event(session):
    mock_session = MagicMock()
    mock_session.get = AsyncMock(return_value=Event(id=1, name='Test Event', description='desc', ticket_price=10.0, tickets_available=100, start_date=datetime.datetime.now(), end_data=datetime.datetime.now(), organization_id=1))
    service = EventService()
    event = await service.get_event(1, mock_session)
    assert event is not None
    assert event.id == 1

@pytest.mark.asyncio
async def test_create_event(session):
    mock_session = MagicMock()
    mock_session.exec = AsyncMock()
    mock_result = MagicMock()
    mock_result.first.return_value = Organization(id=1, name='Org', email='org@email.com', description='desc', created_by=1)
    mock_session.exec.return_value = mock_result
    mock_session.add = MagicMock()
    mock_session.commit = AsyncMock()
    mock_session.refresh = AsyncMock()
    service = EventService()
    event_data = EventCreate(title='Test Event', description='desc', ticket_price=10.0, available_tickets=100, venue='Venue', address='Addr', start_date=datetime.datetime.now(), end_date=datetime.datetime.now(), img_url=None, organization_id=1)
    new_event = await service.create_event(event_data, mock_session, user_id=1)
    assert new_event.name == 'Test Event'

@pytest.mark.asyncio
async def test_get_attendees(session):
    mock_session = MagicMock()
    mock_session.exec = AsyncMock()
    mock_result = MagicMock()
    mock_result.all.return_value = [EventAttendance(user_id=1, event_id=1)]
    mock_session.exec.return_value = mock_result
    service = EventService()
    attendees = await service.get_attendees(1, mock_session)
    assert isinstance(attendees, list)
    assert attendees[0].user_id == 1

@pytest.mark.asyncio
async def test_remove_event(session):
    mock_session = MagicMock()
    mock_session.delete = AsyncMock()
    mock_session.commit = AsyncMock()
    service = EventService()
    service.get_event = AsyncMock(return_value=Event(id=1, name='Test Event', description='desc', ticket_price=10.0, tickets_available=100, start_date=datetime.datetime.now(), end_data=datetime.datetime.now(), organization_id=1))
    status_code = await service.remove_event(1, mock_session)
    assert status_code == status.HTTP_204_NO_CONTENT
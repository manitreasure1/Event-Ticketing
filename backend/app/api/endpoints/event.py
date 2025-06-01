from fastapi import APIRouter, Depends
from app.db.sessions import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from app.services.event_service import EventService


router = APIRouter()
event_service = EventService()


@router.get("/")
async def get_events(session: AsyncSession = Depends(get_session)):
    events = await event_service.get_events(session)
    return events


@router.get("/{event_id}")
async def get_event(event_id: int, session: AsyncSession = Depends(get_session)):
    event = await event_service.get_event(event_id, session)
    return event


@router.delete("/{event_id}")
async def remove_event(event_id: int, session: AsyncSession = Depends(get_session)):
    event = event_service.remove_event(event_id, session)
    return event

# todo
@router.get("/{event_id}/attendees/")
def get_event_attendees(event_id: int, session: AsyncSession = Depends(get_session)):
    get_attendees = event_service.get_attendees(event_id, session)
    return get_attendees


# todo
@router.get("/search/")
def find_events():
    pass


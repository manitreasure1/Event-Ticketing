from fastapi import APIRouter, Depends, Form
from sqlmodel import select
from ..dependencies import get_current_user
from db.sessions import get_session
from services.event_service import EventService
from db.schemas import EventCreate, EventRead
from sqlmodel.ext.asyncio.session import AsyncSession
from db.models import Event, Organization
from typing import Annotated, List

router = APIRouter()
event_service = EventService()

@router.get("/dashboard/")
async def organization_dashboard():
    pass


@router.get("{organization_id}/events/", response_model=List[EventRead])
async def organization_events(organization_id: int, session: AsyncSession = Depends(get_session)):
    result =  await session.exec(select(Event).where(Event.organization_id == organization_id))
    org_events = result.all()
    return org_events


# ! must use current organization Id
@router.post("/events", response_model=EventRead)
async def create_event(*,
                  event: Annotated[EventCreate, Form()],
                  session: AsyncSession = Depends(get_session),
                  current_user = Depends(get_current_user)
                  ):
    add_event = await event_service.create_event(event, session, current_user.id)
    return add_event


# @router.get("/events/{event_id}")
# async def organization_event(*, event_id):
#     pass

# @router.patch("/events/{event_id}/update")
# async def organization_event_update(*, event_id):
#     pass
# @router.delete("/events/{event_id}/update")
# async def organization_event_delete(event_id):
#     pass

# @router.get("/tickets/")
# async def get_tickets():
#     pass




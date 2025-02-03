from fastapi import APIRouter, Depends, Form, HTTPException, status
from sqlmodel import select
from ..dependencies import get_current_user
from db.sessions import get_session
from services.event_service import EventService
from db.schemas import EventCreate, EventRead
from sqlmodel.ext.asyncio.session import AsyncSession
from db.models import Event, Organization, UserDb
from typing import Annotated, List


router = APIRouter()
event_service = EventService()


@router.get("{organization_id}/dashboard/")
async def organization_dashboard(organization_id: int, session: AsyncSession = Depends(get_session) ):
    org_data = await session.get(Organization, organization_id)
    if not org_data:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Organization not found')
    org_events =  await session.exec(select(Event).where(Event.organization_id == organization_id))
    
    return {"events": org_events.all()}


@router.post("/events", response_model=EventRead)
async def create_event(*,
                  event: Annotated[EventCreate, Form()],
                  session: AsyncSession = Depends(get_session),
                  current_user = Depends(get_current_user)
                  ):
    add_event = await event_service.create_event(event, session, current_user.id)
    return add_event







from fastapi import APIRouter, Depends, Form, HTTPException, status
from sqlmodel import select
from ..dependencies import get_current_user
from app.db.sessions import get_session
from app.services.event_service import EventService
from app.db.schemas import EventCreate, EventRead
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.models import Event, Organization
from typing import Annotated


router = APIRouter()
event_service = EventService()


# @router.get("{organization_id}/dashboard/")
# async def organization_dashboard(organization_id: int, session: AsyncSession = Depends(get_session) ):
#     org_data = await session.get(Organization, organization_id)
#     if not org_data:
#         raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Organization not found')
#     org_events =  await session.exec(select(Event).where(Event.organization_id == organization_id))
    
#     return {"events": org_events.all()}


@router.post("/create/event/", response_model=EventRead)
async def create_event(*,
                  event: Annotated[EventCreate, Form()],
                  session: AsyncSession = Depends(get_session),
                  current_user = Depends(get_current_user)
                  ):
    print(event)
    try:
        add_event = await event_service.create_event(event, session, current_user.id)
        return {"new_event": add_event,
                 "message": "Event created successfully"}
    except Exception as e:
        print(e)






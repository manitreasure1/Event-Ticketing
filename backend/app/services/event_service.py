from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.models import Event, EventAttendance, Organization
from sqlmodel import select
from fastapi import HTTPException, status
from app.db.schemas import EventCreate


class EventService:
    async def get_events(self, session: AsyncSession):
        eventdb = await session.exec(select(Event))
        if not eventdb:
            raise HTTPException(status.HTTP_204_NO_CONTENT, detail='Empty, Events are not ready yet!')
        result = eventdb.all()
        return result
    

    async def get_event(self, event_id: int, session: AsyncSession):
        event = await session.get(Event, event_id)
        return event
    
    
    async def create_event(self, event: EventCreate, session: AsyncSession, user_id: int):
        result = await session.exec(
            select(Organization).where(
                Organization.id == event.organization_id,
                Organization.created_by == user_id
                ))
        organization = result.first()
        if not organization:
            raise HTTPException(status.HTTP_403_FORBIDDEN, detail="You are not allowed to create an event for this organization")
        new_event = Event(
            name=event.title,
            description=event.description,
            ticket_price=event.ticket_price,
            tickets_available=event.available_tickets,
            venue=event.venue,
            address=event.address,
            start_date=event.start_date,
            end_data=event.end_date,
            image_urls=event.img_url,
            organization_id=event.organization_id
        )
        session.add(new_event)
        await session.commit()
        await session.refresh(new_event)
        return new_event
    
    async def get_attendees(self, event_id: int, session: AsyncSession):
        query = await session.exec(select(EventAttendance).where(EventAttendance.event_id == event_id))
        if not query:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No event Found')
        return query.all()

        pass
    # ! Not fully implemented
    async def remove_event(self, event_id: int, session: AsyncSession):
        event = await self.get_event(event_id, session)
        await session.delete(event)
        await session.commit()
        return status.HTTP_204_NO_CONTENT
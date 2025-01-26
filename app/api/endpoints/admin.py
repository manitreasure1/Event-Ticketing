from fastapi import APIRouter
from sqlmodel import select
from db.models import Organization, UserDb, Event
from sqlmodel.ext.asyncio.session import AsyncSession


router = APIRouter()


@router.get("/dashboard")
async def admin_dashboard():
    pass

@router.get("/users/")
async def get_users(session: AsyncSession):
    statement = select(UserDb)
    result = await session.exec(statement)
    users = result.all()
    return users

@router.get("/users/{user_id}")
async def get_user(user_id):
    pass

@router.post("/users/{user_id}")
async def block_user(user_id):
    pass


@router.get("/organizations")
async def get_organizations(session: AsyncSession):
    statement = select(Organization)
    result = await session.exec(statement)
    organization = result.all()
    return organization


@router.get("/events")
async def get_events(session: AsyncSession):
    statement = select(Event)
    result = await session.exec(statement)
    events =result.all()
    return events


@router.get("/reports")
async def get_reports():
    pass
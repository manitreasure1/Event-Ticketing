from fastapi import APIRouter, UploadFile, File, Depends, Form, HTTPException, status
from typing import Annotated, List
from sqlmodel.ext.asyncio.session import AsyncSession
from app.services.organization_service import OrganizationService
from app.db.sessions import get_session
from ..dependencies import get_current_user
from app.db.schemas import OrganizationCreate, UserUpdate, OrganizationRead
from app.services.user_service import UserService
from sqlmodel import select
from app.db.models import Organization, UserDb, UserOrganization, Event, Ticket


router = APIRouter()
user_service = UserService()
organization_service = OrganizationService()


@router.get("/me")
async def current_user(user = Depends(get_current_user)):
    return user


@router.patch("/update", response_model=UserUpdate)
async def update_user_profile(
    data: Annotated[UserUpdate, Form()],
    session: AsyncSession = Depends(get_session),
    current_user = Depends(get_current_user)
    ):
    updateusr = await user_service.update_user(data, session, current_user)
    return updateusr


@router.patch("/update_img")
async def update_user_img(
    file: Annotated[UploadFile, File()],
    session: AsyncSession = Depends(get_session),
    current_user = Depends(get_current_user)
    ):
    userdb = await user_service.get_user_by_email(current_user.email, session)
    if not userdb:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="user not found")
    file_content = await file.read()
    current_user.image_url = file_content
    session.add(userdb)
    await session.commit()
    await session.refresh(userdb)


@router.get("/me/organizations/", response_model=List[OrganizationRead])
async def my_organization(current_user= Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    result = await session.exec(
        select(Organization)
        .join(UserOrganization, UserOrganization.organization_id == Organization.id) # type: ignore
        .join(UserDb, UserDb.id == UserOrganization.user_id) # type: ignore
        .where(UserDb.username == current_user.username)
        )
    user_orgs = result.all()
    return user_orgs


@router.get("/me/events/")
async def attending_events(current_user= Depends(get_current_user), session: AsyncSession = Depends(get_session)):
    ressult = await session.exec(
        select(Event)
        .join(Ticket, Ticket.event_id == Event.id) #type: ignore
        .join(UserDb, UserDb.id == Ticket.user_id) #type: ignore
        .where(UserDb.username == current_user.username)
    )
    user_attending_events = ressult.all()
    return user_attending_events
    


@router.post("/register/organization/", response_model=OrganizationRead, status_code=status.HTTP_201_CREATED)
async def register_organization(
    data: Annotated[OrganizationCreate, Form()],
    session: AsyncSession = Depends(get_session),
    current_user = Depends(get_current_user)
    ):    
    register_org = await organization_service.create_organization(data, session, current_user.id)
    return register_org



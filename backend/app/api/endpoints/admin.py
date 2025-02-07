
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlmodel import select
from app.db.models import Organization, UserDb, Event
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.sessions import get_session


router = APIRouter()


@router.get("/dashboard")
async def admin_dashboard(session: AsyncSession = Depends(get_session)):
    users = await session.exec(select(UserDb))
    organizations = await session.exec(select(Organization))
    events = await session.exec(select(Event))
    return JSONResponse(
        content={
            "users": users.all(),
            "organizations": organizations.all(),
            "events": events.all()
        }
    )
    
    
@router.get("/users/{user_id}")
async def get_user(user_id:int, session: AsyncSession =Depends(get_session)):
    user = await session.get(UserDb, user_id)
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="user not found")
    return user


@router.patch("/block_user/{user_id}")
async def block_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await get_user(user_id, session)
    user.is_active = not user.is_active
    await session.commit()
    await session.refresh(user)

    action = "blocked" if not user.is_active else "unblocked"
    return {"message": f"User {user.email} has been {action}"}
    


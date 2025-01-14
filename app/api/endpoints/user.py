from fastapi import APIRouter, UploadFile, File, Depends, Form
from typing import Annotated
from db.sessions import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from db.schemas import SignUpScheme
from sqlmodel.ext.asyncio.session import AsyncSession
from services.user_service import UserService

router = APIRouter()

# @router.get("{user_id}/profile")
# def get_user_profile(user_id: int, session: AsyncSession = Depends(get_db)):
#     user_db = UserService.get_user(user_id, session)
#     return user_db

@router.patch("/profile")
def update_user_profile():
    pass

@router.delete("{user_id}")
def delete_user():
    pass

# @router.post("/upload/")
# def upload_user_image(data: Annotated[UploadFile, File(description="user image")]):
#     return data.filename




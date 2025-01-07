from fastapi import APIRouter, UploadFile, File, Depends
from typing import Annotated
from db.sessions import get_session
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/upload/")
def upload_user_image(data: Annotated[UploadFile, File(description="user image")]):
    return data.filename

@router.get("{user_id}")
def get_user(user_id: int):
    return user_id


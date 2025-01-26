from fastapi import APIRouter, UploadFile, File, Depends, Form
from typing import Annotated
from ..dependencies import get_current_user
from db.schemas import UpdateUserRequest



router = APIRouter()

@router.get("/me")
def current_user(user = Depends(get_current_user)):
    return user


@router.patch("/update")
def update_user_profile(
    file: Annotated[UploadFile, File()],
      data: Annotated[UpdateUserRequest, Form()]
    ):
    pass
    
@router.get("/me/events/")
async def my_registered_events():
    pass    




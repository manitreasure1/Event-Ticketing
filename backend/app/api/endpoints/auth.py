
from fastapi import APIRouter, Form, Depends, status
from typing import Annotated
from app.services.user_service import UserService
from app.services.auth_service import AuthService
from app.db.schemas import SignUpScheme, LoginRequest
from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.sessions import get_session
from app.api.dependencies import RefreshTokenBearer


router = APIRouter()
user_services = UserService()
auth_services = AuthService()
refresh_token = RefreshTokenBearer()


@router.post("/login/")
async def login(*, data: Annotated[LoginRequest, Form()], session: AsyncSession = Depends(get_session)):
    login_user = await auth_services.login(data, session)
    return login_user


@router.post("/register/", status_code=status.HTTP_201_CREATED)
async def sign_up(*, data: Annotated[SignUpScheme, Form()], session: AsyncSession = Depends(get_session)):
    sign_up_data = await auth_services.sign_up(data, session)
    return sign_up_data


@router.get("/token/refresh/")
async def get_new_access_token(token_details: dict = Depends(refresh_token)):   
    new_access_token = auth_services.get_new_access_token(token_details)
    return new_access_token


#  todo
@router.delete("/logout/")
async def logout():
    pass




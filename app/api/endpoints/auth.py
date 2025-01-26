from tkinter import N
from fastapi import APIRouter, Form, Depends, status, HTTPException
from typing import Annotated
from db.models import UserDb
from services.user_service import UserService
from services.auth_service import AuthService
from db.schemas import SignUpScheme, LoginRequest
from sqlmodel.ext.asyncio.session import AsyncSession
from db.sessions import get_session
from fastapi.responses import JSONResponse
from api.dependencies import RefreshTokenBearer
from datetime import datetime


router = APIRouter()
user_services = UserService()
auth_services = AuthService()
refresh_token = RefreshTokenBearer()


@router.post("/login/")
async def login(*, data: Annotated[LoginRequest, Form()], session: AsyncSession = Depends(get_session)):
    res = LoginRequest.model_validate(data)
    result = await user_services.get_user_by_email(res.email, session)

    if result is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    if not auth_services.verify_password(res.password, result.hashed_password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
    
    token_data = {"sub": res.email, "user_id": result.id, "role": result.role}

    access_token = auth_services.create_access_token(user_data=token_data)
    refresh_token = auth_services.create_refresh_token(user_data=token_data)
    return JSONResponse(content={
                            "message": "Login successfully",
                            "access_token": access_token,
                            "refresh_token":refresh_token, 
                            "user":{
                                "email": result.email,
                                "id": result.id
                            }
                         })

@router.post("/register/", status_code=status.HTTP_201_CREATED)
async def sign_up(*, data: Annotated[SignUpScheme, Form()], session: AsyncSession = Depends(get_session)):
    user_data = SignUpScheme.model_validate(data)  
    existing_user = await user_services.existing_user(user_data.email, session)
    if existing_user:
        return HTTPException(status.HTTP_403_FORBIDDEN, detail="Email already registered")
    password= auth_services.hash_password(user_data.password)
    new_user = UserDb(
        firstname=user_data.firstname,
        lastname= user_data.lastname,
        username = user_data.email.split("@")[0],
        email=user_data.email,
        hashed_password=password

    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return {"message": "User created successfully", "user_id": new_user.id}


@router.get("/token/refresh/")
async def get_new_access_token(token_details: dict = Depends(refresh_token)):   
    expire_timestamp = token_details.get('exp', False)
    if datetime.fromtimestamp(expire_timestamp) > datetime.now():
        new_access_token = auth_services.create_access_token(user_data=token_details)
        return JSONResponse( content={"access_token": new_access_token})

    return HTTPException(status.HTTP_400_BAD_REQUEST, detail="invalid or expire token")


@router.delete("/logout/")
async def logout():
    pass


@router.post("/register/organization/")
async def register_organization():
    pass

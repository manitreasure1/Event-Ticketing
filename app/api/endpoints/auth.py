
from fastapi import APIRouter, Form, Depends, status, HTTPException
from typing import Annotated
from db.models import UserDb
from services.user_service import UserService
from services.auth_service import AuthService
from db.schemas import SignUpScheme, LoginRequest, TokenResponse
from sqlmodel.ext.asyncio.session import AsyncSession
from db.sessions import get_session

router = APIRouter()
user_services = UserService()
auth_services = AuthService()

@router.post("/login/", response_model=TokenResponse)
async def login(*, data: Annotated[LoginRequest, Form()], session: AsyncSession = Depends(get_session)):
    result = await user_services.get_user_by_email(data.email, session)
    if result is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password A")
    if not auth_services.verify_password(data.password, result.hashed_password):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password B")
    token_data = {"sub": data.email, "user_id": result.id}
    access_token = auth_services.create_access_token(token_data)
    print(access_token)
    return TokenResponse(access_token=access_token)


@router.post("/signup")
async def sign_up(*, data: Annotated[SignUpScheme, Form()], session: AsyncSession = Depends(get_session)):
    user_data = SignUpScheme.model_validate(data)  
    existing_user = await user_services.existing_user(user_data.email, session)
    if existing_user:
        return HTTPException(status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    password= auth_services.hash_password(user_data.password)
    new_user = UserDb(
        username = user_data.fistname+user_data.lastname,
        email=user_data.email,
        hashed_password=password
    )
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return {"message": "User created successfully", "user_id": new_user.id}

# todo: signout
@router.delete("/logout")
async def logout():
    pass

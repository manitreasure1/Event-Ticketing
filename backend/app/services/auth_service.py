from sqlmodel.ext.asyncio.session import AsyncSession
from app.db.schemas import LoginRequest, SignUpScheme
from app.services.user_service import UserService
from fastapi import HTTPException, status
from app.core.utils import Utils
from fastapi.responses import JSONResponse
from app.db.models import UserDb
from datetime import datetime


user_service = UserService()
utils = Utils()


class AuthService:
    async def sign_up(self, data: SignUpScheme, session: AsyncSession):
        existing_user = await user_service.existing_user(data.email, session)
        if existing_user:
            raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Email already registered")
        password= utils.hash_password(data.password)
        new_user = UserDb(
            firstname=data.firstname,
            lastname=data.lastname,
            username =data.email.split("@")[0],
            email=data.email,
            hashed_password=password
        )
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        return {"message": "User created successfully", "user_id": new_user.id}


    async def login(self, data: LoginRequest, session: AsyncSession ):
        result = await user_service.get_user_by_email(data.email, session)
        if result is None:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
        if not utils.verify_password(data.password, result.hashed_password):
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password")
        token_data = {"sub": data.email, "user_id": result.id, "role": result.role}
        access_token = utils.create_access_token(user_data=token_data)
        refresh_token = utils.create_refresh_token(user_data=token_data)
        return JSONResponse(content={
                            "message": "Login successfully",
                            "access_token": access_token,
                            "refresh_token":refresh_token, 
                            "user":{
                                "email": result.email,
                                "id": result.id
                            }
                         })
    
    
    async def get_new_access_token(self, token_details: dict):   
        expire_timestamp = token_details.get('exp', False)
        if datetime.fromtimestamp(expire_timestamp) > datetime.now():
            new_access_token = utils.create_access_token(user_data=token_details)
            return JSONResponse( content={"access_token": new_access_token})

        return HTTPException(status.HTTP_400_BAD_REQUEST, detail="invalid or expire token")
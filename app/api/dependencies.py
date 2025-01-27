from typing import Any
from fastapi import Depends, Request, status
from fastapi.security.http import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from fastapi.exceptions import HTTPException
from app.services.user_service import UserService
from app.db.sessions import get_session
from app.db.models import UserDb
from app.services.auth_service import AuthService
from sqlmodel.ext.asyncio.session import AsyncSession


auth_service = AuthService()
user_service = UserService()


class TokenBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)
    
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | dict:
        creds = await super().__call__(request)
        token_data = auth_service.decode_token(token=creds.credentials)

        if not self.verify_token(creds.credentials):
            raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Invalid or Expired token")

        self.verify_token_data(token_data)
        return token_data

    def verify_token(self, token: str) -> bool:
        try:
            token_data = auth_service.decode_token(token)
            return bool(token_data)
        except Exception:  
            return False
    
    def verify_token_data(self, token_data: dict) -> None:
        raise NotImplementedError("You must override this method in subclasses!")


class AccessTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if token_data.get("refresh", False): 
            raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Provide an access token")


class RefreshTokenBearer(TokenBearer):
    def verify_token_data(self, token_data: dict) -> None:
        if not token_data.get("refresh", False):
            raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Provide a refresh token")


async def get_current_user(
        user_details: dict = Depends(AccessTokenBearer()),
        session: AsyncSession = Depends(get_session)
        ):
    user_email = user_details.get('sub', None)
    user = await user_service.get_user_by_email(user_email=user_email, session=session)
    return user 


class RoleChecker:
    def __init__(self, allowed_roles: list[str]) -> None:
        self.allowed_roles = allowed_roles

    def __call__(self, user_role:UserDb = Depends(get_current_user)) -> Any:
        if  user_role.role in self.allowed_roles:
            return True 
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="You are not permitted to use this route!")
                 
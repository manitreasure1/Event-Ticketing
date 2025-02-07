
from typing import Any
from fastapi import Depends, Request, status
from fastapi.security.http import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer
from fastapi.exceptions import HTTPException
from app.services.user_service import UserService
from app.db.sessions import get_session
from app.db.models import UserDb
from app.core.utils import Utils
from sqlmodel.ext.asyncio.session import AsyncSession
import logging


logger = logging.getLogger(__name__)

utils = Utils()
user_service = UserService()

class TokenBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super().__init__(auto_error=auto_error)
    
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | dict:
        try:
            creds = await super().__call__(request)
            token_data = utils.decode_token(token=creds.credentials) # type: ignore
            if not self.verify_token(creds.credentials): # type: ignore
                raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Invalid or Expired token")
            self.verify_token_data(token_data)
            return token_data
        except ValueError as e:
            logger.error(f"Token Error: {e}")
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail=str(e))
        except Exception as e:
            logger.exception("Unexpected error while validating token.")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An unexpected error occurred while processing the token.",
            )


    def verify_token(self, token: str) -> bool:
        try:
            token_data = utils.decode_token(token)
            return bool(token_data)
        except ValueError as e:
            logger.error(f"Token verification failed: {e}")
            return False
        except Exception as e:  
            logger.error(f"Unexpected error during token verification: {e}")
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
    if not user_email:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    user = await user_service.get_user_by_email(user_email=user_email, session=session)
    if not user.is_active: # type: ignore
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Your account is inactive. Contact support.")
    return user 


class RoleChecker:
    def __init__(self, allowed_roles: list[str]) -> None:
        self.allowed_roles = allowed_roles

    def __call__(self, user_role:UserDb = Depends(get_current_user)) -> Any:
        if  user_role.role in self.allowed_roles:
            return True 
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="You are not permitted !")
                 
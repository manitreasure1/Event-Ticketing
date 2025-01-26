
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
import jwt
from core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"])


class AuthService:
    def __init__(self) -> None:
        self.secret_key = settings.SECRET_KEY
        self.algorithm = settings.ALGORITHM
        self.access_token_expire_hours = settings.ACCESS_TOKEN_EXPIRE_HOURS
        self.refresh_token_expire_days = settings.REFRSH_TOKEN_EXPIRE_DAYS

    def hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, user_data: dict) -> str:
        to_encode = user_data.copy()
        expire = datetime.now() + timedelta(hours=self.access_token_expire_hours)
        to_encode.update({"exp": expire, "refresh": False})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt
    

    def create_refresh_token(self, user_data: dict) -> str:
        to_encode = user_data.copy()
        expire = datetime.now() + timedelta(days=self.refresh_token_expire_days)
        to_encode.update({"exp": expire, "refresh": True})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt


    def decode_token(self, token: str) -> dict:
        try:
            payload = jwt.decode(jwt=token, key=self.secret_key, algorithms=[self.algorithm])
            return payload
        except jwt.ExpiredSignatureError:
            raise ValueError("Token has expired. Please login again.") 
        except jwt.InvalidTokenError:
            raise ValueError("Invalid token")
        
    



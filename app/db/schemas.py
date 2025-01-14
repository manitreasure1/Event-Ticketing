from pydantic import BaseModel, EmailStr, ValidationError
from typing import Optional

class UpdateUserRequest(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    image_url: Optional[str] = None

class SignUpScheme(BaseModel):
    fistname: str
    lastname: str
    email: EmailStr
    password:str
    model_config = {'extra':'forbid'}

class CreateOrganizationScheme(BaseModel):
    name: str
    email: EmailStr
    description: str | None
    model_config = {'extra':'forbid'}

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    model_config = {'extra':'forbid'}

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
  

try:
    SignUpScheme()
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    
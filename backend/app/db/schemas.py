from datetime import datetime
from pydantic import BaseModel, EmailStr, ValidationError
from typing import Optional
from datetime import datetime

"""
# * user schemas 
"""
class UserBase(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    image_url: Optional[str] = None
    role: Optional[str] = 'user'

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    hashed_password: Optional[str] = None
    model_config = {'extra':'forbid'}

class UpdateUserImg(BaseModel):
    image_url: Optional[bytes] = None
    model_config = {'extra':'forbid'}

class UserPublic(UserBase):
    id: int



"""
#  * auth schemas 
"""
class LoginRequest(BaseModel):
    email: EmailStr
    password: str
    model_config = {'extra':'forbid'}

class SignUpScheme(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str
    model_config = {'extra':'forbid'}



"""
# todo: organization schemas 
"""
class OrganizationBase(BaseModel):
    name: str
    email: EmailStr
    description: str | None
    
class OrganizationCreate(OrganizationBase):
    pass

class OrganizationRead(OrganizationBase):
    id: int
    name: str
    email: str
    description: str
    image_url: str | None = None
    created_by: str | int
    # events: list 
    

"""
#  * event schemas
"""
class EventBase(BaseModel):
    title: str
    description: str
    # img_url : Optional[bytes] = None
    ticket_price: float
    available_tickets: int
    venue: Optional[str] = None
    address: Optional[str] = None
    start_date: datetime
    end_date: datetime


    
class EventCreate(EventBase):
    organization_id: int



class EventRead(EventBase):
    id: int
    organization_id: int
    model_config = {'extra':'forbid'}




"""
#  admin schemas 
"""
class AdminBase(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    role: str = 'admin'
    image_url: Optional[str] = None

class AdminCreate(AdminBase):
    password: str

class AdminUpdate(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[EmailStr] = None
    role: Optional[str] = None
    hashed_password: Optional[str] = None
    model_config = {'extra':'forbid'}

class UpdateAdminImg(BaseModel):
    image_url: Optional[bytes] = None
    model_config = {'extra':'forbid'}

class AdminPublic(AdminBase):
    id: int
    model_config = {'extra':'forbid'}

    
"""
#  todo : ticket schemas 
"""
class TicketBase(BaseModel):
    eventId: int | str
    email: EmailStr
    tel: str | int
    paymentMethod: int | str

class PurchaseTicket(TicketBase):
    cardNumber: int | str
    cardHolderName: str
    expiryDate: str | datetime
    cvv: int | str
    model_config={'extra': 'forbid'}

try:
    EventCreate()  # type: ignore
    PurchaseTicket() # type: ignore
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
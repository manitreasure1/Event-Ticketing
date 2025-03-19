from datetime import datetime
from pydantic import BaseModel, EmailStr, ValidationError
from typing import Optional, List
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
    description: str | None = None
    
class OrganizationCreate(OrganizationBase):
    pass

class OrganizationRead(OrganizationBase):
    id: int
    image_url: str | None = None
    created_by: str | int
    
    

"""
#  * event schemas
"""
class EventBase(BaseModel):
    title: str
    description: str
    img_url : Optional[bytes] = None
    ticket_price: float
    available_tickets: int
    venue: Optional[str] = None
    address: Optional[str] = None
    start_date: datetime
    end_date: datetime
    # total_tickets: int
  
class EventCreate(EventBase):
    organization_id: int
    

class EventRead(BaseModel):
    new_event: dict | tuple
    message: str
    model_config = {'extra':'forbid'}


# class EventReadOrg(EventBase):
#     id: int
#     name: str
#     organization_id: int



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
    event_id: int 
    email: EmailStr
    tel: str | int
    payment_method: int | str


class PurchaseTicket(TicketBase):
    card_number: int | str
    card_holder_name: str
    expiry_date: str | datetime
    cvv: int | str
    model_config={'extra': 'forbid'}

    

    # multiple
# class OrganizationWithEventsRead(BaseModel):
#     organization: OrganizationRead
#     events: List[EventReadOrg] = []

try:
    # OrganizationWithEventsRead() 
    EventCreate()  # type: ignore
    PurchaseTicket() # type: ignore
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
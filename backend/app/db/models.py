
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from pydantic import EmailStr


class UserDb(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    firstname: str
    lastname: str
    username: str = Field(index=True)
    image_url: Optional[bytes] = None
    email: EmailStr
    role: str = Field(default='user')
    hashed_password: str = Field(exclude=True)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now)
    last_login:datetime = Field(default=datetime.now())

    organizations: List["UserOrganization"] = Relationship(back_populates="user", cascade_delete=True)
    events: List["EventAttendance"] = Relationship(back_populates="user", cascade_delete=True)
    tickets: List["Ticket"] = Relationship(back_populates="user", cascade_delete=True)


class Organization(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    image_url: Optional[str] = None
    email: EmailStr
    description: Optional[str]
    created_by: Optional[int] = Field(foreign_key="userdb.id", ondelete='CASCADE')
    events: List["Event"] = Relationship(back_populates="organizer", cascade_delete=True)


class UserOrganization(SQLModel, table=True):
    user_id: int = Field(foreign_key="userdb.id", primary_key=True)
    organization_id: int = Field(foreign_key="organization.id", primary_key=True)

    user: "UserDb" = Relationship(back_populates="organizations")



class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str
    image_urls: Optional[bytes] = None
    start_date: datetime 
    end_data: datetime
    ticket_price: float
    tickets_available: int
    total_tickets: int = Field(default=100)
    venue: Optional[str] = None
    address: Optional[str] = None
    organization_id: int = Field(foreign_key="organization.id", ondelete='CASCADE')

    organizer: "Organization" = Relationship(back_populates="events")
    attendants: List["EventAttendance"] = Relationship(back_populates="event", cascade_delete=True)
    tickets: List["Ticket"] = Relationship(back_populates="event", cascade_delete=True)


class EventAttendance(SQLModel, table=True):
    user_id: int = Field(foreign_key="userdb.id", primary_key=True)
    event_id: int = Field(foreign_key="event.id", primary_key=True)
    check_in_time: Optional[datetime] = None

    user: "UserDb" = Relationship(back_populates="events")
    event: "Event" = Relationship(back_populates="attendants")


class Ticket(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    event_id: int = Field(foreign_key="event.id")
    user_id: int = Field(foreign_key="userdb.id")
    qr_code: Optional[str] = None
    status: str = Field(default="available")
    purchase_time: Optional[datetime] = Field(default_factory=datetime.now)

    user: "UserDb" = Relationship(back_populates="tickets")
    event: "Event" = Relationship(back_populates="tickets")




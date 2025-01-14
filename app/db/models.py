from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from pydantic import EmailStr, ValidationError


class UserDb(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    image_url: Optional[str] = None
    email: EmailStr
    hashed_password: str
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.now)
    last_login: Optional[datetime] = None

    organizations: List["UserOrganization"] = Relationship(back_populates="user")
    events: List["EventAttendance"] = Relationship(back_populates="user")
    tickets: List["Ticket"] = Relationship(back_populates="user")


class Organization(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    image_url: Optional[str] = None
    email: EmailStr
    description: str
    created_by: Optional[int] = Field(foreign_key="userdb.id")

    members: List["UserOrganization"] = Relationship(back_populates="organization")
    events: List["Event"] = Relationship(back_populates="organizer")


class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str
    image_urls: Optional[str] = None
    date: datetime
    ticket_price: float
    tickets_available: int
    total_tickets: int = Field(default=100)
    venue: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    organization_id: int = Field(foreign_key="organization.id")

    organizer: "Organization" = Relationship(back_populates="events")
    attendants: List["EventAttendance"] = Relationship(back_populates="event")
    tickets: List["Ticket"] = Relationship(back_populates="event")


class UserOrganization(SQLModel, table=True):
    user_id: int = Field(foreign_key="userdb.id", primary_key=True)
    organization_id: int = Field(foreign_key="organization.id", primary_key=True)

    user: "UserDb" = Relationship(back_populates="organizations")
    organization: "Organization" = Relationship(back_populates="members")


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



try:
    UserDb()
    Event()
    Organization()
    Ticket()
    EventAttendance()
    UserOrganization()
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from pydantic import EmailStr


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    image_url: Optional[str] = None  
    email: EmailStr
    hashed_password: str
    is_active: bool = Field(default=True)

    organizations: List["UserOrganization"] = Relationship(back_populates="user")
    events: List["EventAttendance"] = Relationship(back_populates="user")


class Organization(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    image_url: Optional[str] = None 
    email: EmailStr 
    description: str

    members: List["UserOrganization"] = Relationship(back_populates="organization")
    events: List["Event"] = Relationship(back_populates="organizer")


class Event(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    description: str
    image_urls: Optional[List[str]] = None
    date: datetime
    ticket_price: float
    tickets_available: int
    organization_id: int = Field(foreign_key="organization.id")

    organizer: Organization = Relationship(back_populates="events")
    attendants: List["EventAttendance"] = Relationship(back_populates="event")


class UserOrganization(SQLModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    organization_id: int = Field(foreign_key="organization.id", primary_key=True)

    user: User = Relationship(back_populates="organizations")
    organization: Organization = Relationship(back_populates="members")


class EventAttendance(SQLModel, table=True):
    user_id: int = Field(foreign_key="user.id", primary_key=True)
    event_id: int = Field(foreign_key="event.id", primary_key=True)

    user: User = Relationship(back_populates="events")
    event: Event = Relationship(back_populates="attendants")

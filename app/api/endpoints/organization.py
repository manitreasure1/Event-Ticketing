from fastapi import APIRouter, Form
from typing import Annotated
from app.db.schemas import CreateOrganizationScheme

router = APIRouter()


@router.get("/dashboard/")
async def organization_dashboard():
    pass


@router.get("/events/")
async def organization_events():
    pass

@router.post("/events")
def create_organization(data: Annotated[CreateOrganizationScheme, Form()]):
    return data

@router.get("/events/{event_id}")
async def organization_event(event_id):
    pass

@router.patch("/events/{event_id}/update")
async def organization_event_update(event_id):
    pass
@router.delete("/events/{event_id}/update")
async def organization_event_delete(event_id):
    pass

@router.get("/tickets/")
async def get_tickets():
    pass


@router.get("/{organization_id}/members")
def get_organization_members():
    pass

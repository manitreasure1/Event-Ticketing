from fastapi import APIRouter, Form
from typing import Annotated
from db.schemas import CreateOrganizationScheme

router = APIRouter()

@router.get("/")
def get_organizations():
    pass

@router.post("/")
def create_organization(data: Annotated[CreateOrganizationScheme, Form()]):
    return data


@router.get("{organization_id}")
def get_organization():
    pass

@router.delete("{organization_id}")
def delete_organization():
    pass


@router.get("/{organization_id}/menbers")
def get_organization_members():
    pass

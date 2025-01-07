from fastapi import APIRouter, Form
from typing import Annotated
from db.schemas import CreateOrganizationScheme
router = APIRouter()

@router.post("/")
def create_organization(data: Annotated[CreateOrganizationScheme, Form()]):
    return data

from fastapi import APIRouter, Form
from typing import Annotated
from db.schemas import LoginScheme, SignUpScheme

router = APIRouter()

@router.post("/login/")
def login(data: Annotated[LoginScheme, Form()]):
    return data

@router.post("/sign-up")
def sign_up(data: Annotated[SignUpScheme, Form()]):
    return data


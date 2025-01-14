from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_admins_users():
    pass

@router.get("/organizations")
def get_admins_organizations():
    pass

@router.get("/events")
def get_admins_events():
    pass



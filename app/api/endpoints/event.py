from fastapi import APIRouter

router = APIRouter()


@router.post("/add-event")
def create_event():
    pass

@router.get("/")
def read_events():
    pass


from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def get_events():
    pass

@router.get("/search/")
def find_events():
    pass

@router.get("/{event_id}")
def get_event():
    pass

@router.get("/{event_id}/attendees/")
def get_event_attendees():
    pass


from fastapi import APIRouter

router = APIRouter()


@router.post("/addevent")
def create_event():
    pass

@router.get("/")
def get_events():
    pass

@router.get("/{event_id}")
def get_event():
    pass

@router.patch("/{event_id}")
def upadate_event():
    pass

@router.delete("/{event_id}")
def delete_event():
    pass

@router.get("/attendees")
def get_event_attendees():
    pass


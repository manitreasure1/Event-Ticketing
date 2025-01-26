from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_tickets():
    pass


@router.post("/purchase")
def purchase_ticket():
    pass

@router.get("/{ticket_id}/")
def get_ticket_details():
    pass

@router.get("/{ticket_id}/download/")
def generate_ticket_qrcode():
    pass

@router.post("/{ticket_id}/validate")
def verify_ticket_qrcode():
    pass



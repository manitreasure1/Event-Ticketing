from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def purchase_ticket():
    pass

@router.get("{ticket_id}")
def get_ticket_details():
    pass

@router.get("{ticket_id}/qr")
def generate_ticket_qrcode():
    pass

@router.post("{ticket_id}/verify")
def verify_ticket_qrcode():
    pass



import pytest
from app.utils.generate_qrcode import Qrcode
from cryptography.fernet import Fernet, InvalidToken

@pytest.mark.parametrize("data", ["test123", "another_ticket", "1234567890"])
def test_generate_and_decrypt_qrcode(data):
    key = Fernet.generate_key()
    qr = Qrcode(key)
    enc = qr.generate_ticket_qrcode(data)
    dec = qr.decrypt_generated_qrcode_data(enc)
    assert dec == data

def test_generate_ticket_qrcode_returns_bytes():
    key = Fernet.generate_key()
    qr = Qrcode(key)
    enc = qr.generate_ticket_qrcode("somedata")
    assert isinstance(enc, bytes)

def test_decrypt_generated_qrcode_data_invalid():
    key = Fernet.generate_key()
    qr = Qrcode(key)
    with pytest.raises(InvalidToken):
        qr.decrypt_generated_qrcode_data(b"notavalidtoken")

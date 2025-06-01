import pytest
from app.utils.payments import PaymentMethod


def test_process_payment_not_implemented():
    payment = PaymentMethod()
    with pytest.raises(NotImplementedError):
        payment.process_payment({"amount": 100, "method": "card"})

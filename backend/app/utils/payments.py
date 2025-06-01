class PaymentMethod:

    def process_payment(self, payment_details: dict):
        raise NotImplementedError("process_payment must be implemented by subclasses")

import qrcode
from PIL import Image
import qrcode.console_scripts
import qrcode.constants
from cryptography.fernet import Fernet


class Qrcode:
    def __init__(self, key = Fernet.generate_key()) -> None:
        self.fernet = Fernet(key)

    def generate_ticket_qrcode(self, edata:str):
        print(edata)
        enc_data = self.fernet.encrypt(edata.encode())

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )
        
        qr.add_data(enc_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        # img.save("qr.png")

        # img.show()
        print(enc_data)
        return enc_data


    def decrypt_generated_qrcode_data(self, ddata: bytes):
        dec_data = self.fernet.decrypt(ddata).decode()
        print(dec_data)
        return dec_data

# qr_img = Qrcode()
# data = "trying the qrcode"
# gen = qr_img.generate_ticket_qrcode(data)
# qr_img.decrypt_generated_qrcode_data(gen)
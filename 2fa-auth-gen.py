import time 
import pyotp
import qrcode

key = "Specialkey"

totp = pyotp.TOTP(key)


print(totp.now())

code= totp.now()

if (input_code== code):
    print('True')

else:
    print('False')

uri = pyotp.totp.TOTP(key).provisioning_uri(name="MikeSmith123", issuer_name="Specialkey App")


print(uri)

#QR code to scan
qrcode.make(uri).save("2FA.png") 
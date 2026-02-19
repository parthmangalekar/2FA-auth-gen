import time 
import pyotp
import qrcode

key = "Specialkey"

totp = pyotp.TOTP(key)


print(totp.now())

input_code= input("Enter 2FA Code: ")

code= totp.now()

if (input_code== code):
    print('True')

else:
    print('False')

uri = pyotp.totp.TOTP(key).provisioning_uri(name="MikeSmith123", issuer_name="Specialkey App")

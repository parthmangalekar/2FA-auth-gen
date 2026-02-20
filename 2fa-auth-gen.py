import time 
import pyotp
import qrcode
import os

key = pyotp.random_base32()
print('Your secret key is:', (key))

totp = pyotp.TOTP(key)


uri = pyotp.totp.TOTP(key).provisioning_uri(name="MikeSmith123", issuer_name="Specialkey App")


print('Link: ', uri)

#QR code to scan
cwd = os.getcwd()
print('Your QR code would be saved as 2FA.png at: ' ,cwd, ), qrcode.make(uri).save("2FA.png") 

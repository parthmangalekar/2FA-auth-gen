import pyotp
import qrcode
import os

key = pyotp.random_base32()

totp = pyotp.TOTP(key)


uri = pyotp.totp.TOTP(key).provisioning_uri(name=(input('Username: ')), issuer_name=(input("Issuer's name: ")))

print('Your secret key is:', (key))

print('Link: ', uri)

#QR code to scan
cwd = os.getcwd()
print('Your QR code would be saved as 2FA.png at: ' ,cwd, ), qrcode.make(uri).save("2FA.png") 

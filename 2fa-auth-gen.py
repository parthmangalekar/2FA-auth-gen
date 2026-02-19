import time 
import pyotp

key = "Specialkey"

totp = pyotp.TOTP(key)


print(totp.now())

input_code= input("Enter 2FA Code: ")

code= totp.now()

if (input_code== code):
    print('True')

else:
    print('False')
import time 
import pyotp

key = "Specialkey"

totp = pyotp.TOTP(key)

print(totp.now())
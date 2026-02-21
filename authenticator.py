import pyotp
import time
import sys

key= pyotp.random_base32
totp = pyotp.TOTP(key)

print ('Secret key: ', (key))

try:
    while true:
        current_code= totp.now()
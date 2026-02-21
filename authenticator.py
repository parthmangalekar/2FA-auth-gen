import pyotp
import time
import sys

key= pyotp.random_base32
totp = pyotp.TOTP(key)

print ('Secret key: ', (key))

try:
    while true:
        current_code= totp.now()

        time_remaining= int(30 -(time.time() % 30))

        bar = "/" * (30 - time_remaining) + "-" * time_remaining
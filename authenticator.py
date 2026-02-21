import pyotp
import time
import sys

key= pyotp.random_base32()
totp = pyotp.TOTP(key)

print ('Secret key: ', (key))

try:
    while True:
        current_code= totp.now()

        time_remaining= int(30 -(time.time() % 30))

        bar = "/" * (30 - time_remaining) + "-" * time_remaining

        sys.stdout.write (f"/rTOTP Code: {current_code} | [{bar}] {time_remaining}")
        sys.stdout.flush()

        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopped.")

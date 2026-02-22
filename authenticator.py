import pyotp
import time
import sys 

key= (input('Enter your secret key: ')) 
totp = pyotp.TOTP(key)

print ('Secret key: ', (key)) 
try:
    while True:
        current_code= totp.now()

        time_remaining= int(30 -(time.time() % 30))

        bar = "█" * (30 - time_remaining) + "-" * time_remaining

        print(f"\rCode: {current_code} | [{bar}] {time_remaining}s", end="", flush=True) 

        if time_remaining == 30:
            print()

        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopped.")
import pyotp
import time

print ('-----Authenticator setup-----')
print('Select a method: ')
print("1. Scan QR Code (Coming Soon)")
print("2. Paste Link (Coming Soon)")
print("3. Enter Secret Key")

key= (input('Enter your secret key: ')) 
totp = pyotp.TOTP(key)

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
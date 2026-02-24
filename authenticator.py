import pyotp
import time
import cv2
import os
import pathlib

print ('-----Authenticator setup-----')
print('Select a method: ')
print("1. Scan QR Code (Coming Soon)")
print("2. Paste Link (Coming Soon)")
print("3. Enter Secret Key")

choice = (input('Select a method: '))

if choice =='1':
    AUTO_FILE_NAME= '2FA.png'
    file_path= pathlib.Path.cwd / AUTO_FILE_NAME
    if file_path.exists() and file_path.is_file():
        print('Found', AUTO_FILE_NAME, 'decoding...')
        
        img=cv2.imread(str(file_path))
        detector =cv2.QRCodeDetector()
        

elif choice =='2':
   url= (input('Paste your link here: '))
   try:
       totp = pyotp.parse_uri(url)
   except ValueError:
       print('Invalid link ')
       exit()

elif choice =='3':
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
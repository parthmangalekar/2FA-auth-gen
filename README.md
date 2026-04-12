
TOTP 2FA Toolkit

A collection of Python scripts to generate, verify, and display Time-based One-Time Passwords (TOTP). This toolkit allows you to create your own 2FA credentials, generate scannable QR codes, and run a live authenticator directly in your terminal.
🛠 Features

    Credential Generation: Create random Base32 secret keys and provisioning URIs for use in apps like Google Authenticator or Microsoft Authenticator.

    QR Code Support: Automatically generates a 2FA.png image file for easy mobile syncing.

    Verification System: Test generated codes against the secret key to ensure your implementation is working correctly.

    Terminal Authenticator: A live CLI dashboard that displays the current 6-digit token and a visual countdown bar for the 30-second rotation window.

    Flexible Import: Load your keys via local QR code scanning (OpenCV), provisioning links, or manual key entry.

📦 Requirements

Ensure you have Python installed, then install the necessary dependencies:
Bash

pip install pyotp qrcode opencv-python

Libraries Used:

    pyotp: Manages the TOTP logic and token generation.

    qrcode: Generates the QR code image files.

    opencv-python (cv2): Detects and decodes the QR code from the local image file.

🚀 How to Use
1. Generate a Secret

Run 2fa-auth-gen.py to create a new identity:
Bash

python 2fa-auth-gen.py

    Input your Username and Issuer Name (e.g., "MyService").

    The script will output your Secret Key and a Provisioning Link.

    A file named 2FA.png will be saved to your current directory.

2. Setup/Verification

Run 2fa-verif.py to test if your credentials are valid:
Bash

python 2fa-verif.py

    Select a method (QR, Link, or Key) to load your secret.

    Input the code from your mobile app to check for a True/False match.

3. Terminal Authenticator

Run authenticator.py to use your computer as the 2FA device:
Bash

python authenticator.py

    Option 1 (QR Code): Automatically finds and reads 2FA.png in the current folder.

    Option 2 (Link): Paste the URI generated in step 1.

    Option 3 (Key): Paste the raw Base32 secret key.

    Live View: The script will display a live-updating token and a countdown bar:

        Code: 123456 | [██████████----------] 10s

📂 File Overview
File	Description
2fa-auth-gen.py	Generates secrets, URIs, and the 2FA.png QR image.
2fa-verif.py	A simple verification loop to validate manual inputs.
authenticator.py	The main CLI tool with a live countdown timer and QR decoding.
⚠️ Security Note

Keep your secret_key.enc (when implemented) and 2FA.png files secure. Anyone with access to these can generate your 2FA tokens. Never share your secret Base32 key.

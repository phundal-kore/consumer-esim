Scripts for automating eSIM creation in the Twilio Super SIM platform

**src/reserve-gen-qr-simple.py**
* Simple script that reserves, awaits assignment of activation code, and then generates QR code image for device

**src/reserve-gen-qr-activate.py**
* Similar script to simple, but adds SIM activation and assignment to a fleet.  This script requires a Fleet SID (can be obtained via API or through the console).

**Installation**
1. Clone repo to a local folder
  > git clone https://github.com/phundal-kore/consumer-esim.git
2. Open the consumer-esim folder and install requirements.txt
  > pip install -r requirements.txt
3. Ensure you have set TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN as environmental variables.  These can be retrieved from the console.
4. Execute python
  > python3 src/reserver-gen-qr-simple.py

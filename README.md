Scripts for automating eSIM creation in the Twilio Super SIM platform

**src/reserve-gen-qr-simple.py**
* Simple script that reserves, awaits assignment of activation code, and then generates QR code image for device

**src/reserve-gen-qr-activate.py**
* Similar script to simple, but adds SIM activation and assignment to a fleet.  This script requires a Fleet SID (can be obtained via API or through the console).

import os
import qrcode
import time
from twilio.rest import Client

# setup auth for connecting to Twilio API
# ensure these are set in the environment ahead of running this script
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

# First step is to request the reservation of a profile.  This is done ASYNC
print("Reserving profile")
esim_profile = client.supersim.v1.esim_profiles.create(generate_matching_id='true')

eSid = esim_profile.sid
print("Profile reserved. sid: ",eSid)

print("Awaiting activation code...")

# While this could be done via a callback, for simplicity we will just poll until the profile is created.
while esim_profile.activation_code is None:
    esim_profile = client.supersim.v1.esim_profiles(sid=eSid).fetch()
    time.sleep(2)
    #print ('current: ', esim_profile.activation_code)
    print ('.', end=' ')
print ('Activated')

#Profile is available, now to generate the QR Code
actcode = esim_profile.activation_code.strip()
    
qrstring = 'LPA:' + actcode
print("Activation code: ", qrstring)

#Generate QRcode and save it locally, identified by its SID
qrimg = qrcode.make(qrstring)
qrimg.save('QR-' + esim_profile.sid + '.png')

print('QR code: ' + 'QR-' + esim_profile.sid)


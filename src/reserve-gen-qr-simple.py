import os
import qrcode
import time
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

print("Reserving profile")
esim_profile = client.supersim.v1.esim_profiles.create(generate_matching_id='true')

eSid = esim_profile.sid
print("Profile reserved. sid: ",eSid)

print("Awaiting activation code...")

while esim_profile.activation_code is None:
    esim_profile = client.supersim.v1.esim_profiles(sid=eSid).fetch()
    time.sleep(2)
    #print ('current: ', esim_profile.activation_code)
    print ('.', end=' ')
print ('Activated')
actcode = esim_profile.activation_code.strip()
    
qrstring = 'LPA:' + actcode
print("Activation code: ", qrstring)

qrimg = qrcode.make(qrstring)
qrimg.save('QR-' + esim_profile.sid + '.png')

print('QR code: ' + 'QR-' + esim_profile.sid)


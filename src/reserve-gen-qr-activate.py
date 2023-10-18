import os
import qrcode
import time
from twilio.rest import Client

#Twilio activation parameters.  If activating, you must provide an existing fleet SID.
activate = True
fleet_sid = "HF07d2aad8192630f5992db70de581f2f1"

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
print("Now awaiting creation of activation code...")

# While this could be done via a callback, for simplicity we will just poll until the profile is created.
while esim_profile.activation_code is None:
    esim_profile = client.supersim.v1.esim_profiles(sid=eSid).fetch()
    time.sleep(2)
    print ('.', end = ' ')
print ('Activated')

#Profile is available, now to generate the QR Code and get prepared to activate.
actcode = esim_profile.activation_code.strip()
sim_sid = esim_profile.sim_sid

# Add LPA: string to setup full activation code for QR code    
qrstring = 'LPA:' + actcode
print("Activation code: \n\t", qrstring)

#Generate QRcode and save it locally, identified by its SID
qrimg = qrcode.make(qrstring)
qrimg.save('QR-' + esim_profile.sid + '.png')

print('\nQR code: \n\t' + 'QR-' + esim_profile.sid + ".png")

# (optional) activate eSIM

# set the SIM to a fleet and set to active
if activate:
        esim_profile = client.supersim.v1.sims(sim_sid) \
                        .update(fleet=fleet_sid, status='active')
        print("\n\tDetails of activated sim: ")
        print("\tsid: ",esim_profile.sid)
        print("\tICCID: ", esim_profile.iccid)
        print("\tUnique Name: ", esim_profile.unique_name)

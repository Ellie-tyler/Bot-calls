from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

account_sid = os.getenv("")
auth_token = os.getenv("")
client = Client(account_sid, auth_token)

def make_call(to_number, from_number, webhook_url):
    call = client.calls.create(
        to=to_number,
        from_=from_number,
        url=webhook_url  # This should be your /voice endpoint
    )
    print(f"Call initiated: {call.sid}")

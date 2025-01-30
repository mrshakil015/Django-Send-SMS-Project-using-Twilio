import keys
from twilio.rest import Client

account_sid = keys.account_sid
account_token = keys.auth_token

client = Client(account_sid, account_token)

message = client.messages.create(
    from_=keys.twilio_number,
    body= "Hi this is twilio testion",
    to=keys.my_phone_number
)

print(message.sid)

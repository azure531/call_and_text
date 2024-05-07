from twilio.rest import Client
import keys

client = Client(keys.account_sid,keys.auth_token)

message=client.messages.create(
    body="Gayatri is stuck in a flood. Please stay calm. We're ensuring her safety and will keep you updated.",
    from_=keys.twilio_number,
    to=keys.target_number
)


print(message.body)

call = client.calls.create(
    url='http://demo.twilio.com/docs/voice.xml',  # URL for TwiML instructions
    to=keys.target_number,
    from_=keys.twilio_number
)

print(call.sid)
from twilio.rest import Client
import os

account_sid='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client=Client(account_sid, auth_token)

message=client.messages.create(body='hello this is Niraj recognised by face recogniser.',
            from_='+1xxxxxxxxxx',
            to='+91xxxxxxxxxx'
           )

print(message.sid)
# phone number = +12013553811

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACe43bf579236d2e7b8fec88195cb839c0'
auth_token = '4a6fff57255bbcf0e8951cf865c9dddf'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Hi Manshul, Hows your life going ? You are doing awesome.",
                    from_='+12013553811',
                    to='+36702421566'
                )

print(message.sid)

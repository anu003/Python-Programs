from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC913f7013a71b101c11251f0fe576cc09"
auth_token  = "e5d7795acef3b072885c7cf763ba0c19"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hello!! I love you <3",
    to="+14094446132",    # Replace with your phone number
    from_="+12563990313") # Replace with your Twilio number
print message.sid

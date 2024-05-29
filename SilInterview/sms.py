import africastalking

# Replace these with your Africa's Talking credentials
username = "sandbox"
api_key = "e9807969fb8d58d9e83180349935ae128224f8fc98b0b0088d0a2783f3c4a8d8"

# Initialize the SDK
africastalking.initialize(username, api_key)

# Get the SMS service
sms = africastalking.SMS

try:
    response = sms.send("Hello Message", ["+254702683107"])
    print(response)
except africastalking.AfricasTalkingException as e:
    print(f"Encountered an error while sending: {str(e)}")

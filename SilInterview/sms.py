import africastalking

# Replace these with your Africa's Talking credentials
username = 'SilInterview'  
api_key = '08f5b18ca6898e6996d87b0ccfdc407b8745dc5c0987db03d09060dac228aa62'

# Initialize the SDK
africastalking.initialize(username, api_key)

# Get the SMS service
sms = africastalking.SMS

# Function to send SMS
def send_sms(phone_number, message):
    try:
        response = sms.send(message, [phone_number])
        print(f"SMS sent successfully: {response}")
    except Exception as e:
        print(f"Encountered an error while sending: {e}")

if __name__ == "__main__":
    phone_number = input('Enter phone number (in international format, e.g., +2547xxxxxxx): ')
    send_sms(phone_number, "Kwenda Huko!")

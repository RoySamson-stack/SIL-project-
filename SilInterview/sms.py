import africastalking

# Replace these with your Africa's Talking credentials
username = 'SilInterview'  # For production, use your actual username
api_key = '64709e0a8be635aeda4e1b98742ed8530f101ac2d1ab087aeb8d0a44e46505d0'

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

# Example usage
if __name__ == "__main__":
    phone_number = input('Enter phone number (in international format, e.g., +2547xxxxxxx): ')
    send_sms(phone_number, "Kwenda Huko!")

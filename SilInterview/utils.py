import africastalking
from django.conf import settings

africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)
sms = africastalking.SMS

def send_sms(recipients, message):
    try:
        response = sms.send(message, recipients)
        print(response)
    except Exception as e:
        print(f"Error while sending SMS: {e}")

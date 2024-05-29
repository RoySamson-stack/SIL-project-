import africastalking

africastalking.initialize(
    username='sandbox',
    api_key='e9807969fb8d58d9e83180349935ae128224f8fc98b0b0088d0a2783f3c4a8d8'

)

sms = africastalking.SMS

response = sms.send("Hello Message", ["+254702683107"])
print(response)


def on_finish(error, response):
    if error is not None:
        raise error 
    print(response)    


sms.send("Hello Message", ["+254702683107"], callback=on_finish)    
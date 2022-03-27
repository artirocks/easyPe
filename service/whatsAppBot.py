from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True

    return False

@app.route("/sms", methods=['POST'])
def sms_reply():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    nums = ['1','2','3','4','5','6','7','8','9']

    if 'hi' in incoming_msg:
        # return a welcome message
        welcome = 'Welcome to BBPS easyPe ! \n Please select \n a. Bill Pay \n b. Merchant Offers' 
        msg.body(welcome)
        responded = True

    elif 'a' in incoming_msg:
        # return categoroies
        categories = "Please select Categories ! \n 1. Electricity \n 2. Recharge \n 3. Water \n 4. DTH \n 5. Landline \n 6. LPG Cylinder \n 7. DTH \n 8. Postpaid \n 9. Other"
        tracker["categories"] = True
        msg.body(categories)
        responded = True

    elif 'b' in incoming_msg:
        # return categoroies
        categories = "Please find latest offers here !"
        tracker["categories"] = True
        msg.body(categories)
        responded = True

    elif containsNumber(incoming_msg):
        # return categoroies
        categories = "Do you want to upload the bill? y/n"
        
        msg.body(categories)
        responded = True

    elif 'y' in incoming_msg:
        bill = "Please upload the bill."
        
        msg.body(bill)
        responded = True

    elif 'n' in incoming_msg:
        info = "Please enter biller & account id"
        












    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask,request
import requests

def sendOtp(phoneNumber):
    headers = {
        "Content-Type":"application/json",
        "ApiKey":""
    }
    data = {
        "PhoneNumber":phoneNumber
    }
    res = requests.post("https://api.igniteauth.in/OTP/sendOTP",headers=headers,json=data)
    return res.text

password = "xUSx9r8DZpmURiNe"

app  = Flask(__name__)

@app.route('/')
def home():
    return "HELLO GDSC"

@app.route('/login',methods =['POST'])
def login():
    postData =  request.json
    phoneNumber = postData.get("phoneNumber")
    otp = sendOtp(phoneNumber)
    print(otp)
    return otp
    
if __name__ == '__main__':
    app.run(debug=True)

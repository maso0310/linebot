# Flask API
from flask import Flask,jsonify,request
app=Flask(__name__)

"""
@app.route("/callback")
def callback():
    return jsonify({'data' : request.url})

if __name__=="__main__":
        app.run()


# 取得隱碼 Code
client_id = 'x7H6Hc6UJlxU3UHFAZNYLp'
callback_url = 'http://127.0.0.1:5000/callback'
URL = f'https://notify-bot.line.me/oauth/authorize?response_type=code&client_id={client_id}&redirect_uri={callback_url}&scope=notify&state=NO_STATE'
print(URL)

"""

# 取得授權 Token
import requests

code = 'DWtz2eEs7RGWGSrN45Q8jg'
client_secret = '9K0wvsz8ewIhFcHJYPGQsq7SgLRILLDg7We6WI4kfzI'
headers = {
    'Content-type': 'application/x-www-form-urlencoded'
}

payload = {
 'code':code,
#  'client_id': client_id, 
 'client_secret': client_secret,
#  'redirect_uri': callback_url,
 'grant_type' : 'authorization_code'   
}

res = requests.post('https://notify-bot.line.me/oauth/token', data = payload, headers = headers)

res.text

# 自動發訊息
token = 'NkfgYMh4WX4SGwLISwhJKCEZJjIvRnPsLPWrJjzYNqH'
headers = {
    'Content-type': 'application/x-www-form-urlencoded',
    'Authorization': f'Bearer {token}'
}

payload = {
 'message':"安安!今天天氣不錯唷唷唷", 
}

res = requests.post('https://notify-api.line.me/api/notify', data = payload, headers = headers)


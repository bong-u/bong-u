import requests as req
from flask import Flask, request, redirect
import json
from urllib.parse import unquote

app = Flask(__name__)

CLIENT_ID = ''
REDIRECT_URI = ''

access_token = ''
access_token_expire = ''
refresh_token = ''
refresh_token_expire = ''

@app.route('/oauth', methods=['GET'])
def oauth():
    global access_token
    global access_token_expire
    global refresh_token
    global refresh_token_expire

    print ('GET /oauth')

    code = request.args['code']

    res = req.post(
        url = 'https://kauth.kakao.com/oauth/token',
        headers = {'Content-Type' : 'application/x-www-form-urlencoded'},
        data = 'grant_type=authorization_code&client_id='+CLIENT_ID+'&redirect_uri='+REDIRECT_URI+'&code='+code
    )

    response = res.json()

    access_token = response['access_token']
    access_token_expire = response['expires_in']
    refresh_token = response['refresh_token']
    refresh_token_expire = response['refresh_token_expires_in']

    return res.text

@app.route('/refresh', methods=['GET'])
def refresh():
    global access_token
    global access_token_expire
    global refresh_token
    global refresh_token_expire

    print ('GET /refresh')

    res = req.post(
        url = 'https://kauth.kakao.com/oauth/token',
        headers = {'Content-Type' : 'application/x-www-form-urlencoded'},
        data = 'grant_type=refresh_token&client_id='+CLIENT_ID+'&refresh_token='+ refresh_token
    )

    response = res.json()

    access_token = response['access_token']
    access_token_expire = response['expires_in']

    if 'refresh_token' in response:
        refresh_token = response['refresh_token']
        refresh_token_expire = response['refresh_token_expires_in']

    return res.text


@app.route('/send', methods=['POST'])
def send():
    global access_token
    global access_token_expire
    global refresh_token
    global refresh_token_expire

    print('POST /send')

    payload = json.loads(unquote(request.data.decode('utf-8')))

    headers = {
        'Content-Type' : 'application/x-www-form-urlencoded',
        'Authorization' : 'Bearer ' + access_token,
        'charset' : 'utf-8'
    }

    data = (
        'template_object={{'
            '"object_type" : "text",'
            '"text": "{0}",'
            '"link": {{'
                '"web_url": "{1}",'
                '"mobile_web_url": "{2}"'
            '}}'
        '}}').format(payload.get('text'),'', '').encode('utf-8')

    res = req.post(
        url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send',
        headers = headers,
        data = data
    )

    return res.text

if __name__ == '__main__':
    app.run(host='localhost', port=80)
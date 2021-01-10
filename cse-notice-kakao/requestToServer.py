import requests, json
from urllib.parse import urlencode

def sendRequest(data):

    data = {'text' : data['text'],
            'web_url' : data['href'],
            'mobile_url' : data['href']
        }

    res = requests.post (
        url = 'http://localhost/send',
        headers = {'Content-Type' : 'application/json' },
        data = json.dumps(data)
    )

    print (res.text)

def refreshRequest():

    res = requests.get (
        url = 'http://localhost/refresh',
        headers = {'Content-Type' : 'application/json' }
    )

    print (res.text)
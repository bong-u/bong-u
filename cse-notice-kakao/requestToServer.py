import requests

def sendRequest(data):
    res = requests.post (
        url = 'http://127.0.0.1:5000/send',
        headers = {'Content-Type' : 'application/json' },
        data = {
            'text' : data['text'],
            'web_url' : data['href'],
            'mobile_url' : data['href']
        }
    )
    
    print (res.text)

def refreshRequest():

    res = requests.get (
        url = 'http://127.0.0.1:5000/refresh',
        headers = {'Content-Type' : 'application/json' }
    )
    
    print (res.text)
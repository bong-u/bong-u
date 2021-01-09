from requestToServer import sendRequest, refreshRequest
from crawler import Crawler

if __name__ == '__main__':
    c = Crawler()
    data = c.crawl()

    if data:
        refreshRequest()

        for i in data:
            print (i)
            sendRequest(i)

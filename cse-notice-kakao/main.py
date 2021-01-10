from requestToServer import sendRequest, refreshRequest
from crawler import Crawler
import datetime

if __name__ == '__main__':
    print ('RUNNING ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    c = Crawler()
    data = c.crawl()

    if data:
        refreshRequest()

        for i in data:
            print (i)
            sendRequest(i)
~                                                                                                 
~                                 
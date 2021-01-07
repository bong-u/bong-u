import sys
import requests
from bs4 import BeautifulSoup

class Crawler:

    def __init__(self):
        self.__file = '/home/ubuntu/csecrawl/recent.txt'
        self.__url_orgin = 'https://computer.cnu.ac.kr'
        self.__recent = ['', '']
        self.__recent_m = ['', '']

        self.__board_attr = [
                'main-mini-wrap main-mini-wrap01',
                'main-mini-wrap main-mini-wrap02']
        self.__board_name = [
                '학사공지',
                '일반공지']

        self.LoadFile()

    def LoadFile(self):
        f = open(self.__file, 'r')
        content = f.read()
        f.close()

        if content == '\n':
            return
        else:
            self.__recent = content.rstrip().split('\n')
        

    def CrawlData(self, n):
        try:
            res = requests.get(self.__url_orgin)
        except Exception as e:
            print(e)
            sys.exit(0)

        soup = BeautifulSoup(res.text, 'html.parser')

        notice = soup.find('div', {'class', self.__board_attr[n]})
        notice = notice.findAll('li')
        
        data = []
        
        for i, el in enumerate(notice):
            url = el.find('a')['href']
            no = url.split('&articleNo=')[1]
            url = self.__url_orgin + url
            
            if i == 0: self.__recent_m[n] = no

            if self.__recent[n] == no: break
                         
            post = {}
            
            post['title'] = el.find('span').text.strip()
            post['description'] = url
            post['color'] = 0x105ab5
   
            data.append(post)
        
        #print (data)
        
        return data
    
    def UpdateFile(self):
        f = open(self.__file, 'w')

        f.write(self.__recent_m[0] + '\n')
        f.write(self.__recent_m[1])

        f.close()

if __name__ == '__main__':

    crawler = Crawler()

    crawler.CrawlData (0)
    crawler.CrawlData (1)
    #crawler.UpdateFile()

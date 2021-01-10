import requests
from bs4 import BeautifulSoup

class Crawler:
    __recent = []
    __FILE_PATH = '/home/bong_u_dev/cse-notice-kakao/recent.txt'

    def __init__(self):
        self.__readFile()

    def crawl(self):

        data = []
        new_recent = ['','']
        res = requests.get ('https://computer.cnu.ac.kr/computer/index.do')

        soup = BeautifulSoup(res.text, 'html.parser')

        for i, board in enumerate(soup.select('div.main-mini-box')[:2]):
            for j, notice in enumerate(board.select('li')):
                href = notice.select_one('a')['href']
                articleNo = notice.select_one('a')['href'].split('articleNo=')[1]
                text = notice.select_one('span').text.strip()

                if j == 0:
                    new_recent[i] = articleNo
                if articleNo == self.__recent[i]:
                    break

                data.append({
                    'href' : href,
                    'text' : text
                })

        self.__writeFile(new_recent)
        return data

    def __readFile(self):

        with open(self.__FILE_PATH, 'r') as f:
            self.__recent = f.read().split(' ')

    def __writeFile(self, new_recent):

        with open(self.__FILE_PATH, 'w') as f:
            f.write(new_recent[0] + ' ' + new_recent[1])
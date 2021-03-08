from bs4 import BeautifulSoup
from urllib.request import urlopen

with urlopen('https://datalab.naver.com/keyword/realtimeList.naver?where=main') as response:
    soup = BeautifulSoup(response, 'html.parser')
    print(soup)
##kimchun
import requests
import requests.exceptions
import webbrowser
from bs4 import BeautifulSoup

url = 'https://sports.news.naver.com/kfootball/club/postList?expertId=gimcheonfc'

r = requests.get(url)
html = r.content
soup = BeautifulSoup(html, 'html.parser')
titles_html = soup.select('.news_list > ul > li > div > a > span')

for i in range(len(titles_html)):
    print(i+1, titles_html[i].text, )
##assist
import requests
from bs4 import BeautifulSoup

k_assist = "https://sports.news.naver.com/kfootball/index"
k_assist_rank = requests.get(k_assist)
k_assist_rank_list = BeautifulSoup(k_assist_rank.content,"html.parser", from_encoding='utf=8')

assist_rank_list = k_assist_rank_list.select('#playerRankingList_kleague_1 > tbody > tr')

print("K 리그 1 개인 도움 순위")

for o in assist_rank_list:
    a = o.select('.blind')[0].text
    b = o.select('.name')[0].text
    c = o.select('.point_blue')[0].text
    print(a,b,c)

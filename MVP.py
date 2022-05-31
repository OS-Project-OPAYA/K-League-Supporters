##assist
import requests
from bs4 import BeautifulSoup

k_mvp = "https://sports.news.naver.com/kfootball/index"
k_mvp_rank = requests.get(k_mvp)
k_mvp_rank_list = BeautifulSoup(k_mvp_rank.content,"html.parser", from_encoding='utf=8')

mvp_rank_list = k_mvp_rank_list.select('#playerRankingList_kleague_2 > tbody > tr')

print("K 리그 1 mvp 선정 순위")

for o in mvp_rank_list:
    a = o.select('.blind')[0].text
    b = o.select('.name')[0].text
    c = o.select('.point_blue')[0].text
    print(a,b,c)

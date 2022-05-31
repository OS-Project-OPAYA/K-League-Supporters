import requests
from bs4 import BeautifulSoup

k_score = "https://sports.news.naver.com/kfootball/index"
k_score_rank = requests.get(k_score)
k_score_rank_list = BeautifulSoup(k_score_rank.content,"html.parser", from_encoding='utf=8')

score_rank_list = k_score_rank_list.select('#playerRankingList_kleague_0 > tbody > tr')

print("K 리그 1 개인 득점 순위")

for o in score_rank_list:
    a = o.select('.blind')[0].text
    b = o.select('.name')[0].text
    c = o.select('.link')[0].text.replace("영상보기", "")
    print(a,b,c)

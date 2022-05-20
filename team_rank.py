import requests
from bs4 import BeautifulSoup

k_league = "https://sports.news.naver.com/kfootball/index"
k_team_rank = requests.get(k_league)
k_team_rank_list = BeautifulSoup(k_team_rank.content,"html.parser", from_encoding='utf=8')

team_rank_list = k_team_rank_list.select('#_team_rank_kleague > table > tbody > tr')

for o in team_rank_list:
    r = o.select('.blind')[0].text
    x = o.select('.name')[0].text
    print(r,x)
    




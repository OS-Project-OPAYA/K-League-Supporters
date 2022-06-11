from tkinter import *

import o as o
import requests
import requests.exceptions
import webbrowser
from bs4 import BeautifulSoup
import tkinter.font


########새창 띄우기 함수#########
def cnwcnw11():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("960x480")
    player.resizable(False, False)

    player.mainloop()
def cnwcnw12():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("Ulsan Stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    labelUlsanT = Label(stadiums, text="문수축구경기장", height=2, font=font0)
    labelUlsanT.pack()

    UlsanS = PhotoImage(file="gif/Stadium/Ulsan_S.gif")
    labelUlsanS = Label(stadiums, image=UlsanS)
    labelUlsanS.pack()

    labelUlsanT = Label(stadiums, text="울산광역시 남구 문수로 44 (옥동)", height=2, font=font1)
    labelUlsanT.pack()

    stadiums.mainloop()
def cnwcnw21():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("960x480")
    player.resizable(False, False)

    player.mainloop()
def cnwcnw22():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    stadiums.mainloop()
def cnwcnw31():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("960x480")
    player.resizable(False, False)

    player.mainloop()
def cnwcnw32():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    stadiums.mainloop()

def cnwcnw41():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("960x480")
    player.resizable(False, False)

    player.mainloop()
def cnwcnw42():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    stadiums.mainloop()

def cnwcnw51():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("960x480")
    player.resizable(False, False)

    player.mainloop()

def cnwcnw52():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    stadiums.mainloop()

def cnwcnw61():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("960x480")
    player.resizable(False, False)

    player.mainloop()

def cnwcnw62():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    stadiums.mainloop()

def cnwcnw71():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("960x480")
    player.resizable(False, False)

    player.mainloop()

def cnwcnw72():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    stadiums.mainloop()

def cnwcnw81():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("960x480")
    player.resizable(False, False)

    player.mainloop()

def cnwcnw82():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    stadiums.mainloop()

def cnwcnw91():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("960x480")
    player.resizable(False, False)

    player.mainloop()

def cnwcnw92():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    stadiums.mainloop()

def cnwcnw101():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("960x480")
    player.resizable(False, False)

    player.mainloop()

def cnwcnw102():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    stadiums.mainloop()

def cnwcnw111():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("960x480")
    player.resizable(False, False)

    player.mainloop()

def cnwcnw112():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    stadiums.mainloop()

def cnwcnw121():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("960x480")
    player.resizable(False, False)

    player.mainloop()

def cnwcnw122():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    stadiums.mainloop()

def createNewWindow0(): ## 새창 띄우기함수
    Ulsan = Toplevel(window)
    Ulsan.title("Ulsan")
    Ulsan.geometry("960x480")
    Ulsan.resizable(True, True)

    frame4 = Frame(Ulsan, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Ulsan, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)

    frame6 = Frame(Ulsan, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    players = Button(frame41,text="선수단 정보",width= 15,height=10, command=cnwcnw11)
    players.pack()
    stadium = Button(frame42,text="경기장 정보",width= 15,height=10, command=cnwcnw12)
    stadium.pack()

    urlU = 'https://sports.news.naver.com/kfootball/club/postList?expertId=253'
    r = requests.get(urlU)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    titles_html = soup.select('.news_list > ul > li > div > a > span')
    for i in range(len(titles_html)):
        label = Label(frame5, text=titles_html[i].text)
        label.pack()
    Ulsan.mainloop()

def createNewWindow1():  ## 새창 띄우기함수
    Jeju = Toplevel(window)
    Jeju.title("Jeju")
    Jeju.geometry("960x480")

    Jeju.resizable(False, False)

    frame4 = Frame(Jeju, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Jeju, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)

    frame6 = Frame(Jeju, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    players = Button(frame41,text="선수단 정보",width= 15,height=10, command=cnwcnw21)
    players.pack()
    stadium = Button(frame42,text="경기장 정보",width= 15,height=10, command=cnwcnw22)
    stadium.pack()

    urlJ = 'https://sports.news.naver.com/kfootball/club/postList?expertId=257'

    r = requests.get(urlJ)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    titles_html = soup.select('.news_list > ul > li > div > a > span')

    for i in range(len(titles_html)):
        label = Label(frame5, text=titles_html[i].text)
        label.pack()

    Jeju.mainloop()

def createNewWindow2(): ## 새창 띄우기함수
    Jeonbuk = Toplevel(window)
    Jeonbuk.title("Jeonbuk")
    Jeonbuk.geometry("960x480")
    Jeonbuk.resizable(False, False)

    frame4 = Frame(Jeonbuk, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Jeonbuk, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)

    frame6 = Frame(Jeonbuk, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    players = Button(frame41,text="선수단 정보",width= 15,height=10, command=cnwcnw31)
    players.pack()
    stadium = Button(frame42,text="경기장 정보",width= 15,height=10, command=cnwcnw32)
    stadium.pack()

    urlJe = 'https://sports.news.naver.com/kfootball/club/postList?expertId=256'

    r = requests.get(urlJe)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    titles_html = soup.select('.news_list > ul > li > div > a > span')

    for i in range(len(titles_html)):
        label = Label(frame5, text=titles_html[i].text)
        label.pack()

    Jeonbuk.mainloop()

def createNewWindow3(): ## 새창 띄우기함수
    Incheon = Toplevel(window)
    Incheon.title("Incheon")
    Incheon.geometry("960x480")
    Incheon.resizable(False, False)

    frame4 = Frame(Incheon, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Incheon, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)

    frame6 = Frame(Incheon, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    players = Button(frame41,text="선수단 정보",width= 15,height=10, command=cnwcnw41)
    players.pack()
    stadium = Button(frame42,text="경기장 정보",width= 15,height=10, command=cnwcnw42)
    stadium.pack()

    urlI = 'https://sports.news.naver.com/kfootball/club/postList?expertId=254'

    r = requests.get(urlI)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    titles_html = soup.select('.news_list > ul > li > div > a > span')

    for i in range(len(titles_html)):
        label = Label(frame5, text=titles_html[i].text)
        label.pack()
    Incheon.mainloop()

def createNewWindow4(): ## 새창 띄우기함수
    Pohang = Toplevel(window)
    Pohang.title("Pohang")
    Pohang.geometry("960x480")
    Pohang.resizable(False, False)

    frame4 = Frame(Pohang, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Pohang, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)

    frame6 = Frame(Pohang, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    players = Button(frame41,text="선수단 정보",width= 15,height=10, command=cnwcnw51)
    players.pack()
    stadium = Button(frame42,text="경기장 정보",width= 15,height=10, command=cnwcnw52)
    stadium.pack()

    urlP = 'https://sports.news.naver.com/kfootball/club/postList?expertId=258'

    r = requests.get(urlP)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    titles_html = soup.select('.news_list > ul > li > div > a > span')

    for i in range(len(titles_html)):
        label = Label(frame5, text=titles_html[i].text)
        label.pack()
    Pohang.mainloop()

def createNewWindow5(): ## 새창 띄우기함수
    Seoul = Toplevel(window)
    Seoul.title("Seoul")
    Seoul.geometry("960x480")
    Seoul.resizable(False, False)

    frame4 = Frame(Seoul, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Seoul, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)

    frame6 = Frame(Seoul, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    players = Button(frame41,text="선수단 정보",width= 15,height=10, command=cnwcnw61)
    players.pack()
    stadium = Button(frame42,text="경기장 정보",width= 15,height=10, command=cnwcnw62)
    stadium.pack()

    urlS = 'https://sports.news.naver.com/kfootball/club/postList?expertId=250'

    r = requests.get(urlS)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    titles_html = soup.select('.news_list > ul > li > div > a > span')

    for i in range(len(titles_html)):
        label = Label(frame5, text=titles_html[i].text)
        label.pack()
    Seoul.mainloop()

def createNewWindow6(): ## 새창 띄우기함수
    Gimcheon = Toplevel(window)
    Gimcheon.title("Gimcheon")
    Gimcheon.geometry("960x480")
    Gimcheon.resizable(False, False)

    frame4 = Frame(Gimcheon, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Gimcheon, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)

    frame6 = Frame(Gimcheon, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    players = Button(frame41,text="선수단 정보",width= 15,height=10, command=cnwcnw71)
    players.pack()
    stadium = Button(frame42,text="경기장 정보",width= 15,height=10, command=cnwcnw72)
    stadium.pack()

    urlKC = 'https://sports.news.naver.com/kfootball/club/postList?expertId=gimcheonfc'

    r = requests.get(urlKC)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    titles_html = soup.select('.news_list > ul > li > div > a > span')

    for i in range(len(titles_html)):
        label = Label(frame5, text=titles_html[i].text)
        label.pack()
    Gimcheon.mainloop()

def createNewWindow7(): ## 새창 띄우기함수
    Suwon = Toplevel(window)
    Suwon.title("Suwon")
    Suwon.geometry("960x480")
    Suwon.resizable(False, False)

    frame4 = Frame(Suwon, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Suwon, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)

    frame6 = Frame(Suwon, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    players = Button(frame41,text="선수단 정보",width= 15,height=10, command=cnwcnw81)
    players.pack()
    stadium = Button(frame42,text="경기장 정보",width= 15,height=10, command=cnwcnw82)
    stadium.pack()

    urlSW = 'https://sports.news.naver.com/kfootball/club/postList?expertId=252'

    r = requests.get(urlSW)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    titles_html = soup.select('.news_list > ul > li > div > a > span')

    for i in range(len(titles_html)):
        label = Label(frame5, text=titles_html[i].text)
        label.pack()
    Suwon.mainloop()

def createNewWindow8(): ## 새창 띄우기함수
    Daegu = Toplevel(window)
    Daegu.title("Daegu")
    Daegu.geometry("960x480")
    Daegu.resizable(False, False)

    frame4 = Frame(Daegu, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Daegu, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)

    frame6 = Frame(Daegu, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    players = Button(frame41,text="선수단 정보",width= 15,height=10, command=cnwcnw91)
    players.pack()
    stadium = Button(frame42,text="경기장 정보",width= 15,height=10, command=cnwcnw92)
    stadium.pack()

    urlDG = 'https://sports.news.naver.com/kfootball/club/postList?expertId=248'

    r = requests.get(urlDG)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    titles_html = soup.select('.news_list > ul > li > div > a > span')

    for i in range(len(titles_html)):
        label = Label(frame5, text=titles_html[i].text)
        label.pack()
    Daegu.mainloop()

def createNewWindow9(): ## 새창 띄우기함수
    SuwonFC = Toplevel(window)
    SuwonFC.title("SuwonFC")
    SuwonFC.geometry("960x480")
    SuwonFC.resizable(False, False)

    frame4 = Frame(SuwonFC, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(SuwonFC, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)

    frame6 = Frame(SuwonFC, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    players = Button(frame41,text="선수단 정보",width= 15,height=10, command=cnwcnw101)
    players.pack()
    stadium = Button(frame42,text="경기장 정보",width= 15,height=10, command=cnwcnw102)
    stadium.pack()

    urlSFC = 'https://sports.news.naver.com/kfootball/club/postList?expertId=542'

    r = requests.get(urlSFC)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    titles_html = soup.select('.news_list > ul > li > div > a > span')

    for i in range(len(titles_html)):
        label = Label(frame5, text=titles_html[i].text)
        label.pack()
    SuwonFC.mainloop()

def createNewWindow10(): ## 새창 띄우기함수
    Gangwon = Toplevel(window)
    Gangwon.title("Gangwon")
    Gangwon.geometry("960x480")
    Gangwon.resizable(False, False)

    frame4 = Frame(Gangwon, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Gangwon, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)

    frame6 = Frame(Gangwon, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    players = Button(frame41,text="선수단 정보",width= 15,height=10, command=cnwcnw111)
    players.pack()
    stadium = Button(frame42,text="경기장 정보",width= 15,height=10, command=cnwcnw112)
    stadium.pack()

    urlG = 'https://sports.news.naver.com/kfootball/club/postList?expertId=315'

    r = requests.get(urlG)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    titles_html = soup.select('.news_list > ul > li > div > a > span')

    for i in range(len(titles_html)):
        label = Label(frame5, text=titles_html[i].text)
        label.pack()
    Gangwon.mainloop()

def createNewWindow11(): ## 새창 띄우기함수
    Seongnam = Toplevel(window)
    Seongnam.title("Seongnam")
    Seongnam.geometry("960x480")
    Seongnam.resizable(False, False)

    frame4 = Frame(Seongnam, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Seongnam, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)

    frame6 = Frame(Seongnam, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    players = Button(frame41,text="선수단 정보",width= 15,height=10, command=cnwcnw121)
    players.pack()
    stadium = Button(frame42,text="경기장 정보",width= 15,height=10, command=cnwcnw122)
    stadium.pack()

    urlSE = 'https://sports.news.naver.com/kfootball/club/postList?expertId=521'

    r = requests.get(urlSE)
    html = r.content
    soup = BeautifulSoup(html, 'html.parser')
    titles_html = soup.select('.news_list > ul > li > div > a > span')

    for i in range(len(titles_html)):
        label = Label(frame5, text=titles_html[i].text)
        label.pack()
    Seongnam.mainloop()

btnList = [None]*12 ##버튼 리스트
fnameList = ["Ulsan.gif","Jeju.gif","Jeonbuk.gif","Incheon.gif", "Pohang.gif","Seoul.gif",
             "Gimcheon.gif","Suwon.gif","Daegu.gif", "SuwonFC.gif", "Gangwon.gif", "Seongnam.gif"]
photoList = [None] * 12
i,k = 0,0
num, r, c=0, 0, 0

window=Tk() ##window 생성
window.title("Kleague")  ##window 제목
window.geometry("1280x750+100-50")  ##window 크기
window.resizable(True, True) ##윈도우 창 크기 조절기능

frame1=Frame(window, relief="solid", bd=2) ##화면나누기
frame1.pack(side="left", fill="both", expand=True)

frame2=Frame(window, relief="solid", bd=2)
frame2.pack(side="right", fill="both", expand=False)

frame3=Frame(window, relief="solid", bd=2,padx= 0)
frame3.pack(side="right", fill="both", expand=True)

frame11=Frame(frame3, relief="groove", bd=2)
frame11.pack(side="top", fill="both", expand=True)

frame12=Frame(frame3, relief="groove", bd=2)
frame12.pack(side="bottom", fill="both", expand=True)

frame13=Frame(frame3, relief="groove", bd=2)
frame13.pack(side="bottom", fill="both", expand=True)

################# frame3에  mvp , 득점, 도움 ###################

font0 = tkinter.font.Font(family="consolas",weight="bold", size = 18)
font1 = tkinter.font.Font(family="consolas", size = 14)

k_mvp = "https://sports.news.naver.com/kfootball/index"
k_mvp_rank = requests.get(k_mvp)
k_mvp_rank_list = BeautifulSoup(k_mvp_rank.content,"html.parser", from_encoding='utf=8')

mvp_rank_list = k_mvp_rank_list.select('#playerRankingList_kleague_2 > tbody > tr')

labelprint5 = Label(frame11, text="mvp 선정 순위",height=2,font=font0)
labelprint5.pack()

for o in mvp_rank_list:
    z = o.select('.blind')[0].text
    x = o.select('.name')[0].text
    v = o.select('.point_blue')[0].text

    mvp = Label(frame11, text=z+" "+x+" "+v, font=font1)
    mvp.pack(side="top")

k_score = "https://sports.news.naver.com/kfootball/index"
k_score_rank = requests.get(k_score)
k_score_rank_list = BeautifulSoup(k_score_rank.content,"html.parser", from_encoding='utf=8')

score_rank_list = k_score_rank_list.select('#playerRankingList_kleague_0 > tbody > tr')

labelprint2 = Label(frame13, text="개인 득점 순위",height=2,font=font0)
labelprint2.pack()

for o in score_rank_list:
    f = o.select('.blind')[0].text
    g = o.select('.name')[0].text
    h = o.select('.link')[0].text.replace("영상보기", "")
    goal = Label(frame13, text=f + " " + g + " " + h, font=font1)
    goal.pack(side="top")

labelprint = Label(frame12, text="개인 도움 순위",height=2,font=font0)
labelprint.pack()

k_assist = "https://sports.news.naver.com/kfootball/index"
k_assist_rank = requests.get(k_assist)
k_assist_rank_list = BeautifulSoup(k_assist_rank.content,"html.parser", from_encoding='utf=8')

assist_rank_list = k_assist_rank_list.select('#playerRankingList_kleague_1 > tbody > tr')
for o in assist_rank_list:
    q = o.select('.blind')[0].text
    w = o.select('.name')[0].text
    e = o.select('.point_blue')[0].text


    labelrank1 = Label(frame12, text=q+" "+w+" "+e, font=font1)
    labelrank1.pack(side="top")

k_league = "https://sports.news.naver.com/kfootball/index"
k_team_rank = requests.get(k_league)
k_team_rank_list = BeautifulSoup(k_team_rank.content, "html.parser", from_encoding='utf=8')

team_rank_list = k_team_rank_list.select('#_team_rank_kleague > table > tbody > tr')

for o in team_rank_list:
    df = o.select('.blind')[0].text
    rt = o.select('.name')[0].text
    ranking = Label(frame1, text=df + " " + rt , font=font1)
    ranking.pack()
#####frame2 팀버튼출력#####

photoList[0] = PhotoImage(file = "gif/" + fnameList[0]) ##photolist에 사진넣음
btnList[0] = Button(frame2, width= 180, height =180, image=photoList[0], command=createNewWindow0) ##버튼에 사진넣고 새창기능 추가
photoList[1] = PhotoImage(file = "gif/" + fnameList[1]) ##photolist에 사진넣음
btnList[1] = Button(frame2, width= 180, height =180, image=photoList[1], command=createNewWindow1) ##버튼에 사진넣고 새창기능 추가
photoList[2] = PhotoImage(file = "gif/" + fnameList[2]) ##photolist에 사진넣음
btnList[2] = Button(frame2, width= 180, height =180, image=photoList[2], command=createNewWindow2) ##버튼에 사진넣고 새창기능 추가
photoList[3] = PhotoImage(file = "gif/" + fnameList[3]) ##photolist에 사진넣음
btnList[3] = Button(frame2, width= 180, height =180, image=photoList[3], command=createNewWindow3) ##버튼에 사진넣고 새창기능 추가
photoList[4] = PhotoImage(file = "gif/" + fnameList[4]) ##photolist에 사진넣음
btnList[4] = Button(frame2, width= 180, height =180, image=photoList[4], command=createNewWindow4) ##버튼에 사진넣고 새창기능 추가
photoList[5] = PhotoImage(file = "gif/" + fnameList[5]) ##photolist에 사진넣음
btnList[5] = Button(frame2, width= 180, height =180, image=photoList[5], command=createNewWindow5) ##버튼에 사진넣고 새창기능 추가
photoList[6] = PhotoImage(file = "gif/" + fnameList[6]) ##photolist에 사진넣음
btnList[6] = Button(frame2, width= 180, height =180, image=photoList[6], command=createNewWindow6) ##버튼에 사진넣고 새창기능 추가
photoList[7] = PhotoImage(file = "gif/" + fnameList[7]) ##photolist에 사진넣음
btnList[7] = Button(frame2, width= 180, height =180, image=photoList[7], command=createNewWindow7) ##버튼에 사진넣고 새창기능 추가
photoList[8] = PhotoImage(file = "gif/" + fnameList[8]) ##photolist에 사진넣음
btnList[8] = Button(frame2, width= 180, height =180, image=photoList[8], command=createNewWindow8) ##버튼에 사진넣고 새창기능 추가
photoList[9] = PhotoImage(file = "gif/" + fnameList[9]) ##photolist에 사진넣음
btnList[9] = Button(frame2, width= 180, height =180, image=photoList[9], command=createNewWindow9) ##버튼에 사진넣고 새창기능 추가
photoList[10] = PhotoImage(file = "gif/" + fnameList[10]) ##photolist에 사진넣음
btnList[10] = Button(frame2, width= 180, height =180, image=photoList[10], command=createNewWindow10) ##버튼에 사진넣고 새창기능 추가
photoList[11] = PhotoImage(file = "gif/" + fnameList[11]) ##photolist에 사진넣음
btnList[11] = Button(frame2, width= 180, height =180, image=photoList[11], command=createNewWindow11) ##버튼에 사진넣고 새창기능 추가

for i in range(0,4) :
    for k in range(0,3) :
        btnList[num].grid(row=r, column=c) ##버튼을 행렬식으로 보이게 넣음
        num+=1
        c+=1
    c=0
    r+=1

window.mainloop()
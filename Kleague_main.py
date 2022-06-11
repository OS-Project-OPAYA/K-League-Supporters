from tkinter import *
import sqlite3
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
    player.geometry("+300-50")

    player.resizable(False, False)

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=18)

    frame1 = Frame(player, relief="solid", bd=2)
    frame1.pack(side="left", fill="both", expand=True)

    frame11 = Frame(frame1, relief="solid", bd=2)
    frame11.pack(side="top", fill="both", expand=True)

    frame12 = Frame(frame1, relief="solid", bd=2)
    frame12.pack(side="bottom", fill="both", expand=True)

    frame2 = Frame(player, relief="solid", bd=2)
    frame2.pack(side="right", fill="both", expand=True)

    frame21 = Frame(frame2, relief="solid", bd=2)
    frame21.pack(side="top", fill="both", expand=True)

    frame22 = Frame(frame2, relief="solid", bd=2)
    frame22.pack(side="bottom", fill="both", expand=True)

    labelf = Label(frame11, text="FW", height=2, font=font0)
    labelf.pack()

    playerF = PhotoImage(file="gif/player/ulsan/ulsan_fw.gif")
    labelplayerF = Label(frame11, image=playerF)
    labelplayerF.pack()

    labelM = Label(frame12, text="MF", height=2, font=font0)
    labelM.pack()

    playerM = PhotoImage(file="gif/player/ulsan/ulsan_mf.gif")
    labelplayerM = Label(frame12, image=playerM)
    labelplayerM.pack()

    labelD = Label(frame21, text="DF", height=2, font=font0)
    labelD.pack()

    playerD = PhotoImage(file="gif/player/ulsan/ulsan_df.gif")
    labelplayerD = Label(frame21, image=playerD)
    labelplayerD.pack()

    labelG = Label(frame22, text="GK", height=2, font=font0)
    labelG.pack()

    playerG = PhotoImage(file="gif/player/ulsan/ulsan_gk.gif")
    labelplayerG = Label(frame22, image=playerG)
    labelplayerG.pack()

    player.mainloop()
def cnwcnw12():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("Ulsan Stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    labelUlsanT = Label(stadiums, text="울산문수축구경기장", height=2, font=font0)
    labelUlsanT.pack()
    UlsanS = PhotoImage(file="gif/Stadium/Ulsan_S.gif")
    labelUlsanS = Label(stadiums, image=UlsanS)
    labelUlsanS.pack()
    labelUlsanP = Label(stadiums, text="울산광역시 남구 문수로 44 (옥동)", height=2, font=font1)
    labelUlsanP.pack()

    stadiums.mainloop()
def cnwcnw21():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("+300-50")

    player.resizable(False, False)

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=18)

    frame1 = Frame(player, relief="solid", bd=2)
    frame1.pack(side="left", fill="both", expand=True)

    frame11 = Frame(frame1, relief="solid", bd=2)
    frame11.pack(side="top", fill="both", expand=True)

    frame12 = Frame(frame1, relief="solid", bd=2)
    frame12.pack(side="bottom", fill="both", expand=True)

    frame2 = Frame(player, relief="solid", bd=2)
    frame2.pack(side="right", fill="both", expand=True)

    frame21 = Frame(frame2, relief="solid", bd=2)
    frame21.pack(side="top", fill="both", expand=True)

    frame22 = Frame(frame2, relief="solid", bd=2)
    frame22.pack(side="bottom", fill="both", expand=True)

    labelf = Label(frame11, text="FW", height=2, font=font0)
    labelf.pack()

    playerF = PhotoImage(file="gif/player/jeju/jeju_fw.gif")
    labelplayerF = Label(frame11, image=playerF)
    labelplayerF.pack()

    labelM = Label(frame12, text="MF", height=2, font=font0)
    labelM.pack()

    playerM = PhotoImage(file="gif/player/jeju/jeju_mf.gif")
    labelplayerM = Label(frame12, image=playerM)
    labelplayerM.pack()

    labelD = Label(frame21, text="DF", height=2, font=font0)
    labelD.pack()

    playerD = PhotoImage(file="gif/player/jeju/jeju_df.gif")
    labelplayerD = Label(frame21, image=playerD)
    labelplayerD.pack()

    labelG = Label(frame22, text="GK", height=2, font=font0)
    labelG.pack()

    playerG = PhotoImage(file="gif/player/jeju/jeju_gk.gif")
    labelplayerG = Label(frame22, image=playerG)
    labelplayerG.pack()

    player.mainloop()
def cnwcnw22():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("Jeju stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    labelJejuT = Label(stadiums, text="제주월드컵경기장", height=2, font=font0)
    labelJejuT.pack()
    JejuS = PhotoImage(file="gif/Stadium/Jeju_S.gif")
    labelJejuS = Label(stadiums, image=JejuS)
    labelJejuS.pack()
    labelJejuP = Label(stadiums, text="제주특별자치도 서귀포시 월드컵로 33 (법환동)", height=2, font=font1)
    labelJejuP.pack()

    stadiums.mainloop()
def cnwcnw31():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("+300-50")

    player.resizable(False, False)

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=18)

    frame1 = Frame(player, relief="solid", bd=2)
    frame1.pack(side="left", fill="both", expand=True)

    frame11 = Frame(frame1, relief="solid", bd=2)
    frame11.pack(side="top", fill="both", expand=True)

    frame12 = Frame(frame1, relief="solid", bd=2)
    frame12.pack(side="bottom", fill="both", expand=True)

    frame2 = Frame(player, relief="solid", bd=2)
    frame2.pack(side="right", fill="both", expand=True)

    frame21 = Frame(frame2, relief="solid", bd=2)
    frame21.pack(side="top", fill="both", expand=True)

    frame22 = Frame(frame2, relief="solid", bd=2)
    frame22.pack(side="bottom", fill="both", expand=True)

    labelf = Label(frame11, text="FW", height=2, font=font0)
    labelf.pack()

    playerF = PhotoImage(file="gif/player/jeonbuk/jeonbuk_fw.gif")
    labelplayerF = Label(frame11, image=playerF)
    labelplayerF.pack()

    labelM = Label(frame12, text="MF", height=2, font=font0)
    labelM.pack()

    playerM = PhotoImage(file="gif/player/jeonbuk/jeonbuk_mf.gif")
    labelplayerM = Label(frame12, image=playerM)
    labelplayerM.pack()

    labelD = Label(frame21, text="DF", height=2, font=font0)
    labelD.pack()

    playerD = PhotoImage(file="gif/player/jeonbuk/jeonbuk_df.gif")
    labelplayerD = Label(frame21, image=playerD)
    labelplayerD.pack()

    labelG = Label(frame22, text="GK", height=2, font=font0)
    labelG.pack()

    playerG = PhotoImage(file="gif/player/jeonbuk/jeonbuk_gk.gif")
    labelplayerG = Label(frame22, image=playerG)
    labelplayerG.pack()

    player.mainloop()
def cnwcnw32():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("Jeonbuk stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    labelJeonbukT = Label(stadiums, text="전주월드컵경기장", height=2, font=font0)
    labelJeonbukT.pack()
    JeonbukS = PhotoImage(file="gif/Stadium/Jeonbuk_S.gif")
    labelJeonbukS = Label(stadiums, image=JeonbukS)
    labelJeonbukS.pack()
    labelJeonbukP = Label(stadiums, text="전라북도 전주시 덕진구 기린대로 1055 (장동)", height=2, font=font1)
    labelJeonbukP.pack()

    stadiums.mainloop()

def cnwcnw41():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("+300-50")

    player.resizable(False, False)

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=18)

    frame1 = Frame(player, relief="solid", bd=2)
    frame1.pack(side="left", fill="both", expand=True)

    frame11 = Frame(frame1, relief="solid", bd=2)
    frame11.pack(side="top", fill="both", expand=True)

    frame12 = Frame(frame1, relief="solid", bd=2)
    frame12.pack(side="bottom", fill="both", expand=True)

    frame2 = Frame(player, relief="solid", bd=2)
    frame2.pack(side="right", fill="both", expand=True)

    frame21 = Frame(frame2, relief="solid", bd=2)
    frame21.pack(side="top", fill="both", expand=True)

    frame22 = Frame(frame2, relief="solid", bd=2)
    frame22.pack(side="bottom", fill="both", expand=True)

    labelf = Label(frame11, text="FW", height=2, font=font0)
    labelf.pack()

    playerF = PhotoImage(file="gif/player/incheon/incheon_fw.gif")
    labelplayerF = Label(frame11, image=playerF)
    labelplayerF.pack()

    labelM = Label(frame12, text="MF", height=2, font=font0)
    labelM.pack()

    playerM = PhotoImage(file="gif/player/incheon/incheon_mf.gif")
    labelplayerM = Label(frame12, image=playerM)
    labelplayerM.pack()

    labelD = Label(frame21, text="DF", height=2, font=font0)
    labelD.pack()

    playerD = PhotoImage(file="gif/player/incheon/incheon_df.gif")
    labelplayerD = Label(frame21, image=playerD)
    labelplayerD.pack()

    labelG = Label(frame22, text="GK", height=2, font=font0)
    labelG.pack()

    playerG = PhotoImage(file="gif/player/incheon/incheon_gk.gif")
    labelplayerG = Label(frame22, image=playerG)
    labelplayerG.pack()

    player.mainloop()
def cnwcnw42():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("Incheon stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    labelIncheonT = Label(stadiums, text="인천축구전용경기장", height=2, font=font0)
    labelIncheonT.pack()
    IncheonS = PhotoImage(file="gif/Stadium/Incheon_S.gif")
    labelIncheonS = Label(stadiums, image=IncheonS)
    labelIncheonS.pack()
    labelIncheonP = Label(stadiums, text="인천광역시 중구 참외전로 246 (도원동)", height=2, font=font1)
    labelIncheonP.pack()

    stadiums.mainloop()

def cnwcnw51():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("+300-50")

    player.resizable(False, False)

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=18)

    frame1 = Frame(player, relief="solid", bd=2)
    frame1.pack(side="left", fill="both", expand=True)

    frame11 = Frame(frame1, relief="solid", bd=2)
    frame11.pack(side="top", fill="both", expand=True)

    frame12 = Frame(frame1, relief="solid", bd=2)
    frame12.pack(side="bottom", fill="both", expand=True)

    frame2 = Frame(player, relief="solid", bd=2)
    frame2.pack(side="right", fill="both", expand=True)

    frame21 = Frame(frame2, relief="solid", bd=2)
    frame21.pack(side="top", fill="both", expand=True)

    frame22 = Frame(frame2, relief="solid", bd=2)
    frame22.pack(side="bottom", fill="both", expand=True)

    labelf = Label(frame11, text="FW", height=2, font=font0)
    labelf.pack()

    playerF = PhotoImage(file="gif/player/incheon/incheon_fw.gif")
    labelplayerF = Label(frame11, image=playerF)
    labelplayerF.pack()

    labelM = Label(frame12, text="MF", height=2, font=font0)
    labelM.pack()

    playerM = PhotoImage(file="gif/player/incheon/incheon_mf.gif")
    labelplayerM = Label(frame12, image=playerM)
    labelplayerM.pack()

    labelD = Label(frame21, text="DF", height=2, font=font0)
    labelD.pack()

    playerD = PhotoImage(file="gif/player/incheon/incheon_df.gif")
    labelplayerD = Label(frame21, image=playerD)
    labelplayerD.pack()

    labelG = Label(frame22, text="GK", height=2, font=font0)
    labelG.pack()

    playerG = PhotoImage(file="gif/player/incheon/incheon_gk.gif")
    labelplayerG = Label(frame22, image=playerG)
    labelplayerG.pack()

    player.mainloop()

def cnwcnw52():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("Pohang stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    labelPohangT = Label(stadiums, text="포항스틸야드", height=2, font=font0)
    labelPohangT.pack()
    PohangS = PhotoImage(file="gif/Stadium/Pohang_S.gif")
    labelPohangS = Label(stadiums, image=PohangS)
    labelPohangS.pack()
    labelPohangP = Label(stadiums, text="경상북도 포항시 남구 동해안로6213번길 20 (괴동동)", height=2, font=font1)
    labelPohangP.pack()

    stadiums.mainloop()

def cnwcnw61():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("+300-50")

    player.resizable(False, False)

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=18)

    frame1 = Frame(player, relief="solid", bd=2)
    frame1.pack(side="left", fill="both", expand=True)

    frame11 = Frame(frame1, relief="solid", bd=2)
    frame11.pack(side="top", fill="both", expand=True)

    frame12 = Frame(frame1, relief="solid", bd=2)
    frame12.pack(side="bottom", fill="both", expand=True)

    frame2 = Frame(player, relief="solid", bd=2)
    frame2.pack(side="right", fill="both", expand=True)

    frame21 = Frame(frame2, relief="solid", bd=2)
    frame21.pack(side="top", fill="both", expand=True)

    frame22 = Frame(frame2, relief="solid", bd=2)
    frame22.pack(side="bottom", fill="both", expand=True)

    labelf = Label(frame11, text="FW", height=2, font=font0)
    labelf.pack()

    playerF = PhotoImage(file="gif/player/seoul/seoul_fw.gif")
    labelplayerF = Label(frame11, image=playerF)
    labelplayerF.pack()

    labelM = Label(frame12, text="MF", height=2, font=font0)
    labelM.pack()

    playerM = PhotoImage(file="gif/player/seoul/seoul_mf.gif")
    labelplayerM = Label(frame12, image=playerM)
    labelplayerM.pack()

    labelD = Label(frame21, text="DF", height=2, font=font0)
    labelD.pack()

    playerD = PhotoImage(file="gif/player/seoul/seoul_df.gif")
    labelplayerD = Label(frame21, image=playerD)
    labelplayerD.pack()

    labelG = Label(frame22, text="GK", height=2, font=font0)
    labelG.pack()

    playerG = PhotoImage(file="gif/player/seoul/seoul_gk.png")
    labelplayerG = Label(frame22, image=playerG)
    labelplayerG.pack()

    player.mainloop()

def cnwcnw62():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("Seoul stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    labelSeoulT = Label(stadiums, text="서울월드컵경기장", height=2, font=font0)
    labelSeoulT.pack()
    SeoulS = PhotoImage(file="gif/Stadium/Seoul_S.gif")
    labelSeoulS = Label(stadiums, image=SeoulS)
    labelSeoulS.pack()
    labelSeoulP = Label(stadiums, text="서울특별시 마포구 월드컵로 240 (성산동)", height=2, font=font1)
    labelSeoulP.pack()

    stadiums.mainloop()

def cnwcnw71():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("+300-50")

    player.resizable(False, False)

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=18)

    frame1 = Frame(player, relief="solid", bd=2)
    frame1.pack(side="left", fill="both", expand=True)

    frame11 = Frame(frame1, relief="solid", bd=2)
    frame11.pack(side="top", fill="both", expand=True)

    frame12 = Frame(frame1, relief="solid", bd=2)
    frame12.pack(side="bottom", fill="both", expand=True)

    frame2 = Frame(player, relief="solid", bd=2)
    frame2.pack(side="right", fill="both", expand=True)

    frame21 = Frame(frame2, relief="solid", bd=2)
    frame21.pack(side="top", fill="both", expand=True)

    frame22 = Frame(frame2, relief="solid", bd=2)
    frame22.pack(side="bottom", fill="both", expand=True)

    labelf = Label(frame11, text="FW", height=2, font=font0)
    labelf.pack()

    playerF = PhotoImage(file="gif/player/gimcheon/gimcheon_fw.gif")
    labelplayerF = Label(frame11, image=playerF)
    labelplayerF.pack()

    labelM = Label(frame12, text="MF", height=2, font=font0)
    labelM.pack()

    playerM = PhotoImage(file="gif/player/gimcheon/gimcheon_mf.gif")
    labelplayerM = Label(frame12, image=playerM)
    labelplayerM.pack()

    labelD = Label(frame21, text="DF", height=2, font=font0)
    labelD.pack()

    playerD = PhotoImage(file="gif/player/gimcheon/gimcheon_df.gif")
    labelplayerD = Label(frame21, image=playerD)
    labelplayerD.pack()

    labelG = Label(frame22, text="GK", height=2, font=font0)
    labelG.pack()

    playerG = PhotoImage(file="gif/player/gimcheon/gimcheon_gk.gif")
    labelplayerG = Label(frame22, image=playerG)
    labelplayerG.pack()

    player.mainloop()

def cnwcnw72():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("Gimcheon stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    labelGimcheonT = Label(stadiums, text="김천종합운동장", height=2, font=font0)
    labelGimcheonT.pack()
    GimcheonS = PhotoImage(file="gif/Stadium/Gimcheon_S.gif")
    labelGimcheonS = Label(stadiums, image=GimcheonS)
    labelGimcheonS.pack()
    labelGimcheonP = Label(stadiums, text="경상북도 김천시 운동장길 1 (삼락동)", height=2, font=font1)
    labelGimcheonP.pack()

    stadiums.mainloop()

def cnwcnw81():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("+300-50")

    player.resizable(False, False)

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=18)

    frame1 = Frame(player, relief="solid", bd=2)
    frame1.pack(side="left", fill="both", expand=True)

    frame11 = Frame(frame1, relief="solid", bd=2)
    frame11.pack(side="top", fill="both", expand=True)

    frame12 = Frame(frame1, relief="solid", bd=2)
    frame12.pack(side="bottom", fill="both", expand=True)

    frame2 = Frame(player, relief="solid", bd=2)
    frame2.pack(side="right", fill="both", expand=True)

    frame21 = Frame(frame2, relief="solid", bd=2)
    frame21.pack(side="top", fill="both", expand=True)

    frame22 = Frame(frame2, relief="solid", bd=2)
    frame22.pack(side="bottom", fill="both", expand=True)

    labelf = Label(frame11, text="FW", height=2, font=font0)
    labelf.pack()

    playerF = PhotoImage(file="gif/player/suwon/suwon_fw.gif")
    labelplayerF = Label(frame11, image=playerF)
    labelplayerF.pack()

    labelM = Label(frame12, text="MF", height=2, font=font0)
    labelM.pack()

    playerM = PhotoImage(file="gif/player/suwon/suwon_mf.gif")
    labelplayerM = Label(frame12, image=playerM)
    labelplayerM.pack()

    labelD = Label(frame21, text="DF", height=2, font=font0)
    labelD.pack()

    playerD = PhotoImage(file="gif/player/suwon/suwon_df.gif")
    labelplayerD = Label(frame21, image=playerD)
    labelplayerD.pack()

    labelG = Label(frame22, text="GK", height=2, font=font0)
    labelG.pack()

    playerG = PhotoImage(file="gif/player/suwon/suwon_gk.gif")
    labelplayerG = Label(frame22, image=playerG)
    labelplayerG.pack()

    player.mainloop()

def cnwcnw82():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("Suwon stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    labelSuwonT = Label(stadiums, text="수원월드컵경기장", height=2, font=font0)
    labelSuwonT.pack()
    SuwonS = PhotoImage(file="gif/Stadium/Suwon_S.gif")
    labelSuwonS = Label(stadiums, image=SuwonS)
    labelSuwonS.pack()
    labelSuwonP = Label(stadiums, text="경기도 수원시 팔달구 월드컵로 310 (우만동)", height=2, font=font1)
    labelSuwonP.pack()


    stadiums.mainloop()

def cnwcnw91():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("+300-50")

    player.resizable(False, False)

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=18)

    frame1 = Frame(player, relief="solid", bd=2)
    frame1.pack(side="left", fill="both", expand=True)

    frame11 = Frame(frame1, relief="solid", bd=2)
    frame11.pack(side="top", fill="both", expand=True)

    frame12 = Frame(frame1, relief="solid", bd=2)
    frame12.pack(side="bottom", fill="both", expand=True)

    frame2 = Frame(player, relief="solid", bd=2)
    frame2.pack(side="right", fill="both", expand=True)

    frame21 = Frame(frame2, relief="solid", bd=2)
    frame21.pack(side="top", fill="both", expand=True)

    frame22 = Frame(frame2, relief="solid", bd=2)
    frame22.pack(side="bottom", fill="both", expand=True)

    labelf = Label(frame11, text="FW", height=2, font=font0)
    labelf.pack()

    playerF = PhotoImage(file="gif/player/daegu/daegu_fw.gif")
    labelplayerF = Label(frame11, image=playerF)
    labelplayerF.pack()

    labelM = Label(frame12, text="MF", height=2, font=font0)
    labelM.pack()

    playerM = PhotoImage(file="gif/player/daegu/daegu_mf.gif")
    labelplayerM = Label(frame12, image=playerM)
    labelplayerM.pack()

    labelD = Label(frame21, text="DF", height=2, font=font0)
    labelD.pack()

    playerD = PhotoImage(file="gif/player/daegu/daegu_df.gif")
    labelplayerD = Label(frame21, image=playerD)
    labelplayerD.pack()

    labelG = Label(frame22, text="GK", height=2, font=font0)
    labelG.pack()

    playerG = PhotoImage(file="gif/player/daegu/daegu_gk.gif")
    labelplayerG = Label(frame22, image=playerG)
    labelplayerG.pack()

    player.mainloop()

def cnwcnw92():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("Daegu stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    labelDaeguT = Label(stadiums, text="DGB대구은행 파크", height=2, font=font0)
    labelDaeguT.pack()
    DaeguS = PhotoImage(file="gif/Stadium/Daegu_S.gif")
    labelDaeguS = Label(stadiums, image=DaeguS)
    labelDaeguS.pack()
    labelDaeguP = Label(stadiums, text="대구광역시 북구 고성로 191 (고성동3가)", height=2, font=font1)
    labelDaeguP.pack()

    stadiums.mainloop()

def cnwcnw101():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("+300-50")

    player.resizable(False, False)

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=18)

    frame1 = Frame(player, relief="solid", bd=2)
    frame1.pack(side="left", fill="both", expand=True)

    frame11 = Frame(frame1, relief="solid", bd=2)
    frame11.pack(side="top", fill="both", expand=True)

    frame12 = Frame(frame1, relief="solid", bd=2)
    frame12.pack(side="bottom", fill="both", expand=True)

    frame2 = Frame(player, relief="solid", bd=2)
    frame2.pack(side="right", fill="both", expand=True)

    frame21 = Frame(frame2, relief="solid", bd=2)
    frame21.pack(side="top", fill="both", expand=True)

    frame22 = Frame(frame2, relief="solid", bd=2)
    frame22.pack(side="bottom", fill="both", expand=True)

    labelf = Label(frame11, text="FW", height=2, font=font0)
    labelf.pack()

    playerF = PhotoImage(file="gif/player/suwonfc/suwonfc_fw.gif")
    labelplayerF = Label(frame11, image=playerF)
    labelplayerF.pack()

    labelM = Label(frame12, text="MF", height=2, font=font0)
    labelM.pack()

    playerM = PhotoImage(file="gif/player/suwonfc/suwonfc_mf.gif")
    labelplayerM = Label(frame12, image=playerM)
    labelplayerM.pack()

    labelD = Label(frame21, text="DF", height=2, font=font0)
    labelD.pack()

    playerD = PhotoImage(file="gif/player/suwonfc/suwonfc_df.gif")
    labelplayerD = Label(frame21, image=playerD)
    labelplayerD.pack()

    labelG = Label(frame22, text="GK", height=2, font=font0)
    labelG.pack()

    playerG = PhotoImage(file="gif/player/suwonfc/suwonfc_gk.gif")
    labelplayerG = Label(frame22, image=playerG)
    labelplayerG.pack()

    player.mainloop()

def cnwcnw102():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("SuwonFC stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    labelSuwonT = Label(stadiums, text="수원종합운동장", height=2, font=font0)
    labelSuwonT.pack()
    SuwonS = PhotoImage(file="gif/Stadium/SuwonFC_S.gif")
    labelSuwonS = Label(stadiums, image=SuwonS)
    labelSuwonS.pack()
    labelSuwonP = Label(stadiums, text="경기도 수원시 장안구 경수대로 893 (조원동)", height=2, font=font1)
    labelSuwonP.pack()

    stadiums.mainloop()

def cnwcnw111():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("+300-50")

    player.resizable(False, False)

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=18)

    frame1 = Frame(player, relief="solid", bd=2)
    frame1.pack(side="left", fill="both", expand=True)

    frame11 = Frame(frame1, relief="solid", bd=2)
    frame11.pack(side="top", fill="both", expand=True)

    frame12 = Frame(frame1, relief="solid", bd=2)
    frame12.pack(side="bottom", fill="both", expand=True)

    frame2 = Frame(player, relief="solid", bd=2)
    frame2.pack(side="right", fill="both", expand=True)

    frame21 = Frame(frame2, relief="solid", bd=2)
    frame21.pack(side="top", fill="both", expand=True)

    frame22 = Frame(frame2, relief="solid", bd=2)
    frame22.pack(side="bottom", fill="both", expand=True)

    labelf = Label(frame11, text="FW", height=2, font=font0)
    labelf.pack()

    playerF = PhotoImage(file="gif/player/gangwon/gangwon_fw.gif")
    labelplayerF = Label(frame11, image=playerF)
    labelplayerF.pack()

    labelM = Label(frame12, text="MF", height=2, font=font0)
    labelM.pack()

    playerM = PhotoImage(file="gif/player/gangwon/gangwon_mf.gif")
    labelplayerM = Label(frame12, image=playerM)
    labelplayerM.pack()

    labelD = Label(frame21, text="DF", height=2, font=font0)
    labelD.pack()

    playerD = PhotoImage(file="gif/player/gangwon/gangwon_df.gif")
    labelplayerD = Label(frame21, image=playerD)
    labelplayerD.pack()

    labelG = Label(frame22, text="GK", height=2, font=font0)
    labelG.pack()

    playerG = PhotoImage(file="gif/player/gangwon/gangwon_gk.gif")
    labelplayerG = Label(frame22, image=playerG)
    labelplayerG.pack()

    player.mainloop()

def cnwcnw112():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("Gangwon stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    labelGangwonT = Label(stadiums, text="강릉종합운동장", height=2, font=font0)
    labelGangwonT.pack()
    GangwonS = PhotoImage(file="gif/Stadium/Gangwon_S.gif")
    labelGangwonS = Label(stadiums, image=GangwonS)
    labelGangwonS.pack()
    labelGangwonP = Label(stadiums, text="강원도 강릉시 종합운동장길 69 (교동)", height=2, font=font1)
    labelGangwonP.pack()

    stadiums.mainloop()

def cnwcnw121():  ## 새창 띄우기함수
    player = Toplevel(window)
    player.title("player")
    player.geometry("+300-50")

    player.resizable(False, False)

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=18)

    frame1 = Frame(player, relief="solid", bd=2)
    frame1.pack(side="left", fill="both", expand=True)

    frame11 = Frame(frame1, relief="solid", bd=2)
    frame11.pack(side="top", fill="both", expand=True)

    frame12 = Frame(frame1, relief="solid", bd=2)
    frame12.pack(side="bottom", fill="both", expand=True)

    frame2 = Frame(player, relief="solid", bd=2)
    frame2.pack(side="right", fill="both", expand=True)

    frame21 = Frame(frame2, relief="solid", bd=2)
    frame21.pack(side="top", fill="both", expand=True)

    frame22 = Frame(frame2, relief="solid", bd=2)
    frame22.pack(side="bottom", fill="both", expand=True)

    labelf = Label(frame11, text="FW", height=2, font=font0)
    labelf.pack()

    playerF = PhotoImage(file="gif/player/seongnam/seongnam_fw.gif")
    labelplayerF = Label(frame11, image=playerF)
    labelplayerF.pack()

    labelM = Label(frame12, text="MF", height=2, font=font0)
    labelM.pack()

    playerM = PhotoImage(file="gif/player/seongnam/seongnam_mf.gif")
    labelplayerM = Label(frame12, image=playerM)
    labelplayerM.pack()

    labelD = Label(frame21, text="DF", height=2, font=font0)
    labelD.pack()

    playerD = PhotoImage(file="gif/player/seongnam/seongnam_df.gif")
    labelplayerD = Label(frame21, image=playerD)
    labelplayerD.pack()

    labelG = Label(frame22, text="GK", height=2, font=font0)
    labelG.pack()

    playerG = PhotoImage(file="gif/player/seongnam/seongnam_gk.gif")
    labelplayerG = Label(frame22, image=playerG)
    labelplayerG.pack()

    player.mainloop()

def cnwcnw122():  ## 새창 띄우기함수
    stadiums = Toplevel(window)
    stadiums.title("Seongnam stadium")
    stadiums.geometry("960x480")
    stadiums.resizable(False, False)

    labelSeongnamT = Label(stadiums, text="탄천종합운동장", height=2, font=font0)
    labelSeongnamT.pack()
    SeongnamS = PhotoImage(file="gif/Stadium/Seongnam_S.gif")
    labelSeongnamS = Label(stadiums, image=SeongnamS)
    labelSeongnamS.pack()
    labelSeongnamP = Label(stadiums, text="경기도 성남시 분당구 탄천로 215", height=2, font=font1)
    labelSeongnamP.pack()

    stadiums.mainloop()

def createNewWindow0(): ## 새창 띄우기함수
    Ulsan = Toplevel(window)
    Ulsan.title("Ulsan")
    Ulsan.resizable(True, True)

    frame4 = Frame(Ulsan, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Ulsan, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)
    frame5.configure(background='snow')

    frame6 = Frame(Ulsan, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    UlsanSch = PhotoImage(file="gif/schedule/ulsan_s.gif")
    labelUlsanSch = Label(frame6, image=UlsanSch)
    labelUlsanSch.pack()

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    frame41.configure(background='snow')
    frame42.configure(background='snow')

    playerbtn = PhotoImage(file="gif/squad.gif")
    squadbtn = PhotoImage(file="gif/ground.gif")

    players = Button(frame41, image=playerbtn, width=180, height=210, command=cnwcnw11)
    players.pack()
    stadium = Button(frame42, image=squadbtn, width=180, height=150, command=cnwcnw12)
    stadium.pack()

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=14)

    labela = Label(frame5, text="울산 현대 축구단 최신뉴스", height=2, font=font0, background = 'snow')
    labela.pack()

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
    Jeju.resizable(False, False)

    frame4 = Frame(Jeju, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Jeju, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)
    frame5.configure(background='snow')

    frame6 = Frame(Jeju, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    JejuSch = PhotoImage(file="gif/schedule/jeju_s.gif")
    labelJejuSch = Label(frame6, image=JejuSch)
    labelJejuSch.pack()

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    frame41.configure(background='snow')
    frame42.configure(background='snow')

    playerbtn1 = PhotoImage(file="gif/squad.gif")
    squadbtn1 = PhotoImage(file="gif/ground.gif")

    players = Button(frame41, image=playerbtn1, width=180, height=210, command=cnwcnw21)
    players.pack()
    stadium = Button(frame42, image=squadbtn1, width=180, height=150, command=cnwcnw22)
    stadium.pack()

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=14)

    labela = Label(frame5, text="제주 유나이티드 FC 최신뉴스", height=2, font=font0, background = 'snow')
    labela.pack()

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
    Jeonbuk.resizable(False, False)

    frame4 = Frame(Jeonbuk, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Jeonbuk, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)
    frame5.configure(background='snow')

    frame6 = Frame(Jeonbuk, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    JeonbukSch = PhotoImage(file="gif/schedule/jeonbuk_s.gif")
    labelJeonbukSch = Label(frame6, image=JeonbukSch)
    labelJeonbukSch.pack()

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    frame41.configure(background='snow')
    frame42.configure(background='snow')

    playerbtn2 = PhotoImage(file="gif/squad.gif")
    squadbtn2 = PhotoImage(file="gif/ground.gif")

    players = Button(frame41, image=playerbtn2, width=180, height=210, command=cnwcnw31)
    players.pack()
    stadium = Button(frame42, image=squadbtn2, width=180, height=150, command=cnwcnw32)
    stadium.pack()

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=14)

    labela = Label(frame5, text="전북 현대 모터스 최신뉴스", height=2, font=font0, background = 'snow')
    labela.pack()

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
    Incheon.resizable(False, False)

    frame4 = Frame(Incheon, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Incheon, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)
    frame5.configure(background='snow')

    frame6 = Frame(Incheon, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    IncheonSch = PhotoImage(file="gif/schedule/incheon_s.gif")
    labelIncheonSch = Label(frame6, image=IncheonSch)
    labelIncheonSch.pack()

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    frame41.configure(background='snow')
    frame42.configure(background='snow')

    playerbtn3 = PhotoImage(file="gif/squad.gif")
    squadbtn3 = PhotoImage(file="gif/ground.gif")

    players = Button(frame41, image=playerbtn3, width=180, height=210, command=cnwcnw41)
    players.pack()
    stadium = Button(frame42, image=squadbtn3, width=180, height=150, command=cnwcnw42)
    stadium.pack()

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=14)

    labela = Label(frame5, text="인천 유나이티드 FC 최신뉴스", height=2, font=font0, background = 'snow')
    labela.pack()

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
    Pohang.resizable(False, False)

    frame4 = Frame(Pohang, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Pohang, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)
    frame5.configure(background='snow')

    frame6 = Frame(Pohang, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    PohangSch = PhotoImage(file="gif/schedule/pohang_s.gif")
    labelPohangSch = Label(frame6, image=PohangSch)
    labelPohangSch.pack()

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    frame41.configure(background='snow')
    frame42.configure(background='snow')

    playerbtn = PhotoImage(file="gif/squad.gif")
    squadbtn = PhotoImage(file="gif/ground.gif")

    players = Button(frame41, image=playerbtn, width=180, height=210, command=cnwcnw51)
    players.pack()
    stadium = Button(frame42, image=squadbtn, width=180, height=150, command=cnwcnw52)
    stadium.pack()

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=14)

    labela = Label(frame5, text="포항 스틸러스 최신뉴스", height=2, font=font0, background = 'snow')
    labela.pack()

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
    Seoul.resizable(False, False)

    frame4 = Frame(Seoul, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Seoul, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)
    frame5.configure(background='snow')

    frame6 = Frame(Seoul, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    SeoulSch = PhotoImage(file="gif/schedule/seoul_s.gif")
    labelSeoulSch = Label(frame6, image=SeoulSch)
    labelSeoulSch.pack()

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    frame41.configure(background='snow')
    frame42.configure(background='snow')

    playerbtn = PhotoImage(file="gif/squad.gif")
    squadbtn = PhotoImage(file="gif/ground.gif")

    players = Button(frame41, image=playerbtn, width=180, height=210, command=cnwcnw61)
    players.pack()
    stadium = Button(frame42, image=squadbtn, width=180, height=150, command=cnwcnw62)
    stadium.pack()

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=14)

    labela = Label(frame5, text="FC 서울 최신뉴스", height=2, font=font0, background = 'snow')
    labela.pack()

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
    Gimcheon.resizable(False, False)

    frame4 = Frame(Gimcheon, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Gimcheon, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)
    frame5.configure(background='snow')

    frame6 = Frame(Gimcheon, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    GimchunSch = PhotoImage(file="gif/schedule/gimchun_s.gif")
    labelGimchunSch = Label(frame6, image=GimchunSch)
    labelGimchunSch.pack()

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    frame41.configure(background='snow')
    frame42.configure(background='snow')

    playerbtn = PhotoImage(file="gif/squad.gif")
    squadbtn = PhotoImage(file="gif/ground.gif")

    players = Button(frame41, image=playerbtn, width=180, height=210, command=cnwcnw71)
    players.pack()
    stadium = Button(frame42, image=squadbtn, width=180, height=150, command=cnwcnw72)
    stadium.pack()

    font0 = tkinter.font.Font(family="consolos", weight="bold", size=14)

    labela = Label(frame5, text="김천 상무 프로축구단 최신뉴스", height=2, font=font0, background = 'snow')
    labela.pack()

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
    Suwon.resizable(False, False)

    frame4 = Frame(Suwon, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Suwon, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)
    frame5.configure(background='snow')

    frame6 = Frame(Suwon, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    SuwonSch = PhotoImage(file="gif/schedule/suwon_s.gif")
    labelSuwonSch = Label(frame6, image=SuwonSch)
    labelSuwonSch.pack()

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    frame41.configure(background='snow')
    frame42.configure(background='snow')

    playerbtn = PhotoImage(file="gif/squad.gif")
    squadbtn = PhotoImage(file="gif/ground.gif")

    players = Button(frame41, image=playerbtn, width=180, height=210, command=cnwcnw81)
    players.pack()
    stadium = Button(frame42, image=squadbtn, width=180, height=150, command=cnwcnw82)
    stadium.pack()

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=14)

    labela = Label(frame5, text="수원 삼성 최신뉴스", height=2, font=font0, background = 'snow')
    labela.pack()

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
    Daegu.resizable(False, False)

    frame4 = Frame(Daegu, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Daegu, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)
    frame5.configure(background='snow')

    frame6 = Frame(Daegu, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    DaeguSch = PhotoImage(file="gif/schedule/daegu_s.gif")
    labelDaeguSch = Label(frame6, image=DaeguSch)
    labelDaeguSch.pack()

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    frame41.configure(background='snow')
    frame42.configure(background='snow')

    playerbtn = PhotoImage(file="gif/squad.gif")
    squadbtn = PhotoImage(file="gif/ground.gif")

    players = Button(frame41, image=playerbtn, width=180, height=210, command=cnwcnw91)
    players.pack()
    stadium = Button(frame42, image=squadbtn, width=180, height=150, command=cnwcnw92)
    stadium.pack()

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=14)

    labela = Label(frame5, text="대구 FC 최신뉴스", height=2, font=font0, background = 'snow')
    labela.pack()

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
    SuwonFC.resizable(False, False)

    frame4 = Frame(SuwonFC, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(SuwonFC, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)
    frame5.configure(background='snow')

    frame6 = Frame(SuwonFC, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    SuwonFCSch = PhotoImage(file="gif/schedule/suwonfc_s.gif")
    labelSuwonFCSch = Label(frame6, image=SuwonFCSch)
    labelSuwonFCSch.pack()

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    frame41.configure(background='snow')
    frame42.configure(background='snow')

    playerbtn = PhotoImage(file="gif/squad.gif")
    squadbtn = PhotoImage(file="gif/ground.gif")

    players = Button(frame41, image=playerbtn, width=180, height=210, command=cnwcnw101)
    players.pack()
    stadium = Button(frame42, image=squadbtn, width=180, height=150, command=cnwcnw102)
    stadium.pack()

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=14)

    labela = Label(frame5, text="수원 FC 최신뉴스", height=2, font=font0, background = 'snow')
    labela.pack()

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
    Gangwon.resizable(False, False)

    frame4 = Frame(Gangwon, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Gangwon, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)
    frame5.configure(background='snow')

    frame6 = Frame(Gangwon, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    GangwonSch = PhotoImage(file="gif/schedule/gangwon_s.gif")
    labelGangwonSch = Label(frame6, image=GangwonSch)
    labelGangwonSch.pack()

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    frame41.configure(background='snow')
    frame42.configure(background='snow')

    playerbtn = PhotoImage(file="gif/squad.gif")
    squadbtn = PhotoImage(file="gif/ground.gif")

    players = Button(frame41, image=playerbtn, width=180, height=210, command=cnwcnw111)
    players.pack()
    stadium = Button(frame42, image=squadbtn, width=180, height=150, command=cnwcnw112)
    stadium.pack()

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=14)

    labela = Label(frame5, text="강원 FC 최신뉴스",height=2,font=font0, background = 'snow')
    labela.pack()

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
    Seongnam.resizable(False, False)

    frame4 = Frame(Seongnam, relief="solid", bd=2)
    frame4.pack(side="left", fill="both", expand=True)

    frame5 = Frame(Seongnam, relief="solid", bd=2)
    frame5.pack(side="right", fill="both", expand=True)
    frame5.configure(background='snow')

    frame6 = Frame(Seongnam, relief="solid", bd=2)
    frame6.pack(side="right", fill="both", expand=True)

    SeongnamSch = PhotoImage(file="gif/schedule/seongnam_s.gif")
    labelSeongnamSch = Label(frame6, image=SeongnamSch)
    labelSeongnamSch.pack()

    frame41 = Frame(frame4, relief="groove", bd=1)
    frame41.pack(side="top", fill="both", expand=True)

    frame42 = Frame(frame4, relief="groove", bd=1)
    frame42.pack(side="top", fill="both", expand=True)

    frame41.configure(background='snow')
    frame42.configure(background='snow')

    playerbtn = PhotoImage(file="gif/squad.gif")
    squadbtn = PhotoImage(file="gif/ground.gif")

    players = Button(frame41, image=playerbtn, width=180, height=210, command=cnwcnw121)
    players.pack()
    stadium = Button(frame42, image=squadbtn, width=180, height=150, command=cnwcnw122)
    stadium.pack()

    font0 = tkinter.font.Font(family="consolas", weight="bold", size=14)

    labela = Label(frame5, text="성남 FC 최신뉴스", height=2, font=font0, background = 'snow')
    labela.pack()

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

frame01=Frame(frame1, relief="solid", bd=1)
frame01.pack(side="top", fill="both", expand=True)

frame02=Frame(frame1, relief="solid", bd=1)
frame02.pack(side="bottom", fill="both", expand=True)


################# frame3에  mvp , 득점, 도움 ###################

con = sqlite3.connect("kleague_data.db")
cur = con.cursor()

##font
font0 = tkinter.font.Font(family="consolas",weight="bold", size = 18)
font1 = tkinter.font.Font(family="consolas", size = 14)

##mvp rank
k_mvp = "https://sports.news.naver.com/kfootball/index"
k_mvp_rank = requests.get(k_mvp)
k_mvp_rank_list = BeautifulSoup(k_mvp_rank.content,"html.parser", from_encoding='utf=8')

mvp_rank_list = k_mvp_rank_list.select('#playerRankingList_kleague_2 > tbody > tr')

labelprint5 = Label(frame11, text="MVP 선정 순위",height=2,font=font0,background='snow')
labelprint5.pack()

cur.execute("DELETE FROM 'k_league_mvp'")
for o in mvp_rank_list:
    z = o.select('.blind')[0].text
    x = o.select('.name')[0].text
    v = o.select('.point_blue')[0].text

    cur.execute("insert into k_league_mvp values (?, ?, ?)", (z, x, v))
    con.commit()

    mvp = Label(frame11, text=z+" "+x+" "+v, font=font1,background='snow')
    mvp.pack(side="top")



k_score = "https://sports.news.naver.com/kfootball/index"
k_score_rank = requests.get(k_score)
k_score_rank_list = BeautifulSoup(k_score_rank.content,"html.parser", from_encoding='utf=8')

score_rank_list = k_score_rank_list.select('#playerRankingList_kleague_0 > tbody > tr')

labelprint2 = Label(frame13, text="개인 득점 순위",height=2,font=font0,background='snow')
labelprint2.pack()

cur.execute("DELETE FROM 'k_league_score'")
for o in score_rank_list:
    f = o.select('.blind')[0].text
    g = o.select('.name')[0].text
    h = o.select('.link')[0].text.replace("영상보기", "")
    goal = Label(frame13, text=f + " " + g + " " + h, font=font1,background='snow')
    goal.pack(side="top")

    cur.execute("insert into k_league_score values (?, ?, ?)", (f, g, h))
    con.commit()

labelprint = Label(frame12, text="개인 도움 순위",height=2,font=font0, background='snow')
labelprint.pack()

k_assist = "https://sports.news.naver.com/kfootball/index"
k_assist_rank = requests.get(k_assist)
k_assist_rank_list = BeautifulSoup(k_assist_rank.content,"html.parser", from_encoding='utf=8')

assist_rank_list = k_assist_rank_list.select('#playerRankingList_kleague_1 > tbody > tr')

cur.execute("DELETE FROM 'k_league_assist'")
for o in assist_rank_list:
    q = o.select('.blind')[0].text
    w = o.select('.name')[0].text
    e = o.select('.point_blue')[0].text

    cur.execute("insert into k_league_assist values (?, ?, ?)", (q, w, e))
    con.commit()

    labelrank1 = Label(frame12, text=q+" "+w+" "+e, font=font1,background='snow')
    labelrank1.pack(side="top")
k_logo = PhotoImage(file="gif/kleague.gif")
labellogo = Label(frame01, image=k_logo)
labellogo.pack()
frame01.configure(background='snow')
frame02.configure(background='snow')
frame11.configure(background='snow')
frame12.configure(background='snow')
frame13.configure(background='snow')


labelprint20 = Label(frame02, text="K 리그 팀 순위",height=2,font=font0, background='snow')
labelprint20.pack()

k_league = "https://sports.news.naver.com/kfootball/index"
k_team_rank = requests.get(k_league)
k_team_rank_list = BeautifulSoup(k_team_rank.content, "html.parser", from_encoding='utf=8')

team_rank_list = k_team_rank_list.select('#_team_rank_kleague > table > tbody > tr')

cur.execute("DELETE FROM 'k_league_rank'")
for o in team_rank_list:
    df = o.select('.blind')[0].text
    rt = o.select('.name')[0].text
    ranking = Label(frame02, text=df + " " + rt , font=font1,background='snow')
    ranking.pack()

    cur.execute("insert into k_league_rank values (?, ?)", (df, rt))
    con.commit()
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
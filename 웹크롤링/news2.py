# 웹페이지에 들어가지않고 뉴스 검색 엑샐에 담아 저장import requests

import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup
import pandas as pd # 데이터 프레임 만들기 위함

keyword= input("키워드를 검색해주세요 >> ")

r = requests.get("https://news.google.com/search?q="+keyword+"&hl=ko&gl=KR&ceid=KR%3Ako") # %20은 공백   
bs = BeautifulSoup(r.text, "html.parser")

#기사제목, 링크
news = []

# titles = bs.select("div.xrnccd > article > h3 > a")
titles = bs.find_all('div',{"class":"xrnccd"})

# ./articles/CAIiEHfXQrNJJ561lIHLGAs4xm4qGQgEKhAIACoHCAow0__cCjDUitABMP3bjQY?uo=CAUiNmh0dHBzOi8vd3d3Lmhhbmt5dW5nLmNvbS9zb2NpZXR5L2FydGljbGUvMjAyMjA3MTM1OTM0N9IBAA&amp;hl=ko&amp;gl=KR&amp;ceid=KR%3Ako
# .은 현재위치를 나타냄

for i in titles :
    title = i.find("h3").text
    links = "https://news.goolge.com" + i.find("a")["href"][1:]
    #description = i.find("span",{"class":"xBbh9"}).text
    date = i.find("time").text

    google_news_df = pd.DataFrame(news, columns=["기사제목","링크주소","날짜"])
    news.append([title, links, date])

google_news_df.to_excel("C:/Users/theri/OneDrive/바탕 화면/국비학원/뉴스크롤링 결과2.xlsx")

print('저장완료')

#for i in titles :
#    title = i.text
#    links = "https://news.goolge.com" + i.get("href")[1:] #. 은 https://news.goolge.com와 같다
# 1부터인 이유가 앞에 .을 없앨려고
#    news.append([title, links])
#    google_news_df = pd.DataFrame(news, columns=["기사제목","링크주소"])

# print(google_news_df)
# google_news_df.to_excel("C:/Users/theri/OneDrive/바탕 화면/국비학원/뉴스크롤링 결과.xlsx")

# print('저장완료')
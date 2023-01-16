import requests
from bs4 import BeautifulSoup, BeautifulStoneSoup
import pandas as pd # 데이터 프레임 만들기 위함

r = requests.get("https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR2h6Y1dZU0FtdHZLQUFQAQ?hl=ko&gl=KR&ceid=KR%3Ako")
bs = BeautifulSoup(r.text, "html.parser")

#기사제목, 링크
news = []

titles = bs.select("div.xrnccd > article > h3 > a")

# ./articles/CAIiEHfXQrNJJ561lIHLGAs4xm4qGQgEKhAIACoHCAow0__cCjDUitABMP3bjQY?uo=CAUiNmh0dHBzOi8vd3d3Lmhhbmt5dW5nLmNvbS9zb2NpZXR5L2FydGljbGUvMjAyMjA3MTM1OTM0N9IBAA&amp;hl=ko&amp;gl=KR&amp;ceid=KR%3Ako
# .은 현재위치를 나타냄

for i in titles :
    title = i.text
    links = "https://news.goolge.com" + i.get("href")[1:] #. 은 https://news.goolge.com와 같다
# 1부터인 이유가 앞에 .을 없앨려고
    news.append([title, links])
    google_news_df = pd.DataFrame(news, columns=["기사제목","링크주소"])

google_news_df.to_excel("C:/Users/theri/OneDrive/바탕 화면/국비학원/뉴스크롤링 결과.xlsx")

print('저장완료')
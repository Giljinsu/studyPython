import requests
from bs4 import BeautifulSoup

r = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%82%A0%EC%94%A8")
bs = BeautifulSoup(r.content, "html.parser")

whether = bs.select_one("div.temperature_info > dl.summary_list > dd.desc")

print("오늘의 체감온도는 {}도 입니다".format(whether.text))

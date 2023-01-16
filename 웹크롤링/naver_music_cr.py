# 자바스크립트 활성화 문제 발생 selenium으로 해결 해야할듯

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

r= requests.get("https://vibe.naver.com/chart")
bs = BeautifulSoup(r.text, "html.parser")
wd = webdriver.Chrome('./webdriver/chromedriver.exe')

song_name = []
artist_name = []

song = bs.select("content > div:nth-child(2) > div > div > div > div > div > ul > li:nth-child(1) > ul > li:nth-child(1) > div.song_area > div.song > a")
print(song)
#
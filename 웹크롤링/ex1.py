#requests 웹페이지 요소 가져오기
# BeautifulSoup 파싱
 
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.naver.com")
bs = BeautifulSoup(r.content, "html.parser")

# print(r.content) # 받은 자원 확인 16비트로 들어옴 
# print(r.text) #텍스트 형식
h2 = bs.select("h2") # h2 요소 선택
# select_one은 첫번쨰 만 반환

# print(h2)
# print(h2[0].text) #text는 text만 뽑음 select는 인덱스값을 입력해야됨 어떤건지 모르니
# print(h2[0].attrs) 
print(h2)

#h2 = bs.select_one("h2 > a") 자식요소 a 선택

# selector = bs.select_one("div.current_box") # 요소 선택
# selector = bs.select(".title") # title이 포함된 모든 클래스 
# selector = bs.select("#u_skip") # id 선택

# selector = bs.find_all("태그명",{"속성명": "값"}) # find all

selector = bs.find_all("div",{"class": "partner_box"}) # div partner_box 안에 있는 요소들
# find만 사용가능

print(selector)
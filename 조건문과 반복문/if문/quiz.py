web = input("웹사이트를 입력해주세요 >> ")
nation =web.split(".")

if nation[-1] == "kr":
    print("한국입니다")
elif nation[-1] == "uk" :
    print("영국입니다")
elif nation[-1] == "com" :
    print("기업입니다")
elif nation[-1] == "org" :
    print("기관입니다")
else :
    print("알수없음")
#주민번호 성별 확인
number = input("주민번호를 입력하시오")
odd = int(number[7])

if odd%2 == 0 :
    print("여성입니다")
else :
    print("남성입니다")
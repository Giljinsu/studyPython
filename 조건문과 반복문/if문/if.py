# if
# if 조건식:
#   print("조건식이 참일떄 실행할 것") print 앞에 공백은 스페이스 4번이 default


# weather = '비'

# if weather == '비' :
#     print("비가 온다")

study_time = int(input("오늘 공부할 시간 >"))

if study_time >= 3 and study_time < 4 :
    print("그만 쉬시유")
# == if 3<= study_time <4 
else :
    print(f"{3-study_time}시간만 더 하면되유")

potato = "감자"

# def jeju_potato() :
#     print(potato)
#     potato = "고구마" # 에러 같은 이름의 전역 지역변수 같이 사용 불가
#     print(potato)

# jeju_potato()

# 대신 global 선언하면 가능

def jeju_potato() :
    #global potato
    print(potato)
    potato = "고구마"
    print(potato)

jeju_potato()
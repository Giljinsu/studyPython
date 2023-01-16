from datetime import time, datetime, timedelta


# today = date.today()
# print(today)
# new_date = date(1999, 12, 31)
# print(new_date) 날짜

# print(time(9))
# print(time(9,2))
# print(time(9,2,2))
# print(time(9,2,2,2222)) 시간

dt = datetime.now() # 날짜 시간 둘다

print(dt)

dt = datetime(2002, 10, 20, 14, 5 ,2)
print(dt)

# timedelta() 날짜 차이계산

today = datetime.now()

print(today)
print(today - timedelta(days = 20)) # 20일 빼기 
# print(today - timedelta(days = 20)) hours week minutes 사용가능

import time
now = time.time()
print(now) #1977 1월 1일 0시 0분 0초 부터 지금까지의 초

from time import localtime, strftime

now = localtime()
print(now)

# time 모듈의 strftime()
now = strftime("%Y-%m-%d %H:%M") 
print(now)
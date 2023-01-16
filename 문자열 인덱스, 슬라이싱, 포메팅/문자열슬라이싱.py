#print("0123456789"[0:8]) 0부터 8 01234567
str_slice = "0123456789"

print(str_slice[0:7]) # 0123456
#마지막까지 
print(str_slice[0:]) #0123456789
#앞부분 비워놓으면 자동으로 0부터
print(str_slice[:7]) #0123456
#음수
print(str_slice[-8:-1]) #2345678 9는 포함이 안됨

str_slice="python is easy"
#          012345678910111213
print(str_slice[:-1]) #python is eas 까지
#모두 출력
print(str_slice[-14:])
# 2의배수만 출력
str_slice="0123456789"
print(str_slice[0:10:2])
print(str_slice[::-3]) # 9630`

str_a = "python"
print(str_a[0:]+str_a[::-1])
# int() 정수형 변환 소수점 밑자리 버림

from sys import flags


print(int(127.23))
print(int(127,299392))

print(int(True)) # 1
print(int(False)) # 0

#문자열
print(type(int("12345")))
print(int("1234a"))# 정수말고 다른 문자가 들어가면 오류

# float() 실수형
print(float(100))
print(float(3))

print(float(True))
print(float(False))

print(float("23.23242"))
print(float("2323")) # 정수형 문자열도 가능

#str() 문자열
#모든 자료형

print(type(str(123123)))
print(str(3213.232))
print(str(True))
print(str(False))

#bool() 
#모든 자료형

#False
print(bool(0))
print(bool(0.0))
print(bool(""))

#True
print(bool(1))
print(bool(1.0))
print(bool("1234"))


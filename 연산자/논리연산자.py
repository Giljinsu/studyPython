# and 둘다 

print( True and True)
print(True and False)
# ex
print(10>3 and 2>3) # False

# or 둘다 False면 False 나머진 True

#and
print("A" and 10>3 and True and False) # False 마지막것이 반환 False
print("1" and 0 and True and "참") # 도중 false인 0이 반환

# or
print(0 or 0.0 or False or 1) # 1이 나온다

# and or 우선순위
print(True or False and "참") # 참이 나올거 같지만 True가 나옴
# and 연산자가 Or 연산자보다 우선순위가 크기 때문이다

#not 연산자 반대로 뒤집음
print(not(True and True)) # False 나옴``

# 연산자 우선순위 캡처(연산자우선순위.png)으로 저장해놓음

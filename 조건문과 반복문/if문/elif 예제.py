# 3의배수이면서 짝수
from tkinter import N


number = int(input("정수를 입력해주세요 >>"))

if number%3 == 0 and number % 2 ==0 :
    print("3의배수이면서 짝수 입니다")
elif number % 3 != 0:
    print("3의배수가 아닙니다")
else :
    print("짝수가 아닙니다")

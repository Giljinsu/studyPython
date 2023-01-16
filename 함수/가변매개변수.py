def add(num1 , num2=20, num3=40) : #값지정은 1번째 값은 불가능 후에 가능
    return num1+ num2 + num3

print(add(20,num3=2))

# 가변매개변수 * 사용
 
def add(*args) : # args 대신 다른 이름 가능 nums sets   
    sum =0
    for i in args:
        sum += i
    print(sum)

add(10,20,30,40)

#def add(*args, num) : 일반매개변수는 가변매개변수 앞에 올수없다 
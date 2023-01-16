# tuple ()
# tuple은 추가 삭제 수정이 불가능함

numbers = (1,2,3,4)

print(type(numbers))

#괄호 생략 가능
numbers = 1, 2, 3
print(numbers)
# 만약 튜플 numbers= (1) 요소가 1개라면 이대로 사용하면 튜플로 인식 안됨
# 따라서 마지막에 ,를 붙혀줘야함

#튜플 합치기
print(numbers+numbers)
#n 차원 튜플 가능함

print(numbers.index(3)) # 4 위치 찾기

#
number1 = numbers[0]
number2 = numbers[0]
number3 = numbers[0]
# 위에것이랑 같은방식
number1, number2,number3 = numbers

# 주의점
numbers = 1,2,3,4
#number1, number2,number3 = numbers # 에러발생
# 해결방법
number1, number2,number3, _ = numbers # 변수 1개 더 만들어주거나   
number1, number2, *number3 = numbers # 남은변수 담아주는 *

# 추가되는겉처럼 사용
print(id(numbers))
numbers += 5, 6,
print(numbers)
print(id(numbers))# 하지만 id 주소가 다름 즉 새로운 튜플

# for 변수 in 나열가능한 함수 : (나열가능한 함수란 list dictionary range)
#   실행할 문자 

for i in range(1, 10+1) :
    print(i)

fruits = ["사과", "딸기", "바나나"]

for i in fruits:
    print("{}가 들어있습니다".format(i))

sum=0
for i in range(1,30+1) :
    if i%3==0 :
        sum +=i
print(sum)

# same
sum=0
for i in range(3,30+1,3) :
    print("{} + {} = ".format(sum, i), end="") # end 를 주는 이유 \n 없앨라고
    sum +=i
print(sum)

#dictionary
coffee = {"아메리카노" : 2500 , "라떼" : 3000, "자바": 2500}
for i in coffee.items() : # items 사용하여 키 값 모두
    print(i)
# 키값만 keys() 값만 values()

fruits = ["사과", "딸기", "바나나"]

for i in enumerate(fruits) : # enmerate는 인덱스 값을 매겨줌
    print(f"{i[0]+1}번째 과일은 {i[1]}이다")
# 다른방법
for i,j in enumerate(fruits) : # enmerate는 인덱스 값을 매겨줌
    print(f"{i+1}번째 과일은 {j}이다")

# 이중 리스트
list = [[1,2,3],["a","b","c"]]

for i in list :
    for j in i :
        print(j)

for i in range(2,9+1) :
    for j in range(1,10) :
        print(f"{i} x {j} = {i*j}")
    print()
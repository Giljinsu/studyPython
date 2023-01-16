fruits = ["사과", "키위"," 바나나", "사과", "바나나"]
print(fruits)
# fruits.remove("사과") # 모두 삭제가 아닌 앞에 1개만 삭제됨
# print(fruits)

fruit = input("빼낼과일 입력해주세요 >>")

while fruit in fruits:
    fruits.remove(fruit)

print(fruits)
print("{}를 모두 제거했습니다".format(fruit))
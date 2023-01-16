# dictionary {}
from difflib import context_diff


people = {
    "name" : "김길수",
    "phone" : "010.2020.3949"
}
print(people["name"],people["phone"])

books = {"Daniel" : ["인생", "희망"]}
print( books["Daniel"])

#주의점
check = {"1" : "dds", True:"sds"} # 1 과 True는 값이 같음 주의;

#수정 및 추가
coffee={"Java": 2500, "Americano":2500,}
coffee["Java"] =3000 # 수정
coffee["Moca"] = 3000 # 없는거 입력해서 추가
print(coffee)

# 삭제 pop()
coffee.pop("Moca")
print(coffee)

# keys()안에 있는 키 요소들 , values() 값요소들
print(coffee.keys())
# items( ) 키와 값을 튜플로 반환
print(coffee.values())
# in 연산자 안에 존재하는지
print("Hot" in coffee)
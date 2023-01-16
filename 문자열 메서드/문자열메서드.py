text = "www.Google.com"

print(len(text)) #길이

#capitalize() 첫글자 대문자로 바꿔줌
txt_capitalize=text.capitalize() 

print(txt_capitalize)

# 문자열 전체 대문자 upper() 소문자는 lower()
txt_upper=text.upper()
txt_lower=text.lower()
print(txt_upper)
print(txt_lower)

#count, find, index
print(text.count('G')) # G의 발생횟수 1번 대소문자 구별되서 그럼

print(text.find('g')) # g는 7번째 자리에 있다
print(text.find('o',6)) # 두번쨰 o 찾기위함 1번쨰는 5에 있으니 6번째 부터 찾아라
print(text.find('x')) # 존재 x -1

print(text.index('g')) # find와 비슷하지만
# print(text.index('x')) #에러가 뜸 
# find index에 r붙이면 반대로 rfind rindex

#replace() 문자열 치환
print(text.replace("Google", "Naver"))

#split() 문자열을 구분자로 나눠준다 기본값은 공백
print(text.split())
print(text.split('.')) # www.Google.com 에서 .을 기준으로 구분함
print(text.split("oo")) # oo로

# strip() 좌우 공백 없애준다 다만 문자 사이에 있는 공백은 못지워준다.
text2 ="     www.Google.com  "
print(text2.strip()) 
list_lan = ["java", "c", "Python", "Go"]

# append() 리스트 맨 뒤에 제일 마지막 인덱스(-1)에추가

list_lan.append("Ruby")
print(list_lan)

# append() 주의점
list_a=[1,2,3]
list_lan.append(list_a)
print(list_lan) # ['java', 'c', 'Python', 'Go', 'Ruby', [1, 2, 3]] 요소가 아닌
#리스트로 추가가 된다 2차원 인덱스
#이를 방지하기 위해 # extend 사용

# extend() 요소를 추가하는 방법
list_lan = ["java", "c", "Python", "Go"]
list_lan.extend(list_a)
print(list_lan) #['java', 'c', 'Python', 'Go', 1, 2, 3]

#insert(index,data)
list_lan.insert(0,'R')
print(list_lan)

#Pop() 꺼낸다 제일뒤요소 반환해주고 삭제 스택
print(list_lan.pop())
print(list_lan)
#pop() 안에 인덱스를 주면 해당을 삭제후 반환

#remove() 지정한거 삭제
list_lan.remove("Python")
print(list_lan)

#del
del list_lan[4]
print(list_lan)
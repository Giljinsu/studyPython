i = 0

while True :
    print(1)
    break # 바로 빠져나옴

numbers = [10, 200, 300 ,210 ,52]

for i in numbers :
    if i<200 :
        continue
    print("{} 200 이상만 출력".format(i))

list = [[1,2,3],[10,20,30]]

for i in list :
    for j in i :
        print(j) 
        break # 1, 10 이 나오는데 이유가 자신이 속해있는것 만 탈출
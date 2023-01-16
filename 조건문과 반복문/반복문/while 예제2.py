min_num = int(input("최소값 입력 >>"))
max_num = int(input("최대값 입력 >>"))

odd_list = []
even_list = []

num = min_num
n = 0

if min_num < max_num :
    while num < max_num :
        num+=1
        if num % 2 == 0 :
            even_list.append(num)
        else :
            odd_list.append(num)
    print("최댓값과 최솟값사이에 짝수는 {} 이고 홀수는 {} 이다".format(even_list, odd_list))
else :
    print("최댓값 {}이 최솟값{}보다 크지 않습니다".format(max_num,min_num))


# 최대 최소값 찾기

def max_min_search(*args) :
    max = 0
    min = 0
    for i in args :
        if max < i :
            max = i
        else :
            min = i
    print(max , min)

max_min_search(15,23,62,23,6,8,231,52)


def max_min_search(*args) :
    return max(args), min(args)

max_min_search(15,23,62,23,6,8,231,52)

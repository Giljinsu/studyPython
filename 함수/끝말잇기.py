def game(text1) :
    print(text1)
    text2 = input("끝말을 이어주세요 >>")
    if text1[-1] == text2[0] :
        game(text2)
    else :
        print("끝말이 이어지지 않았습니다")

start = input("처음을 입력해주세요 >>")
game(start)

# 



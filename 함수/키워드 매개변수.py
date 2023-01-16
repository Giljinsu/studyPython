def star_player(**kwargs) :
    for i in kwargs.items : # kwargs만 사용하면 키워드만 나옴 
        print(i)

star_player(축구 = "손흥민", 야구 = "이승엽", 농구 = "허재")

#ex

# 순서 def func(name, *args, address="한국", **kwargs) 이 순서대로 사용


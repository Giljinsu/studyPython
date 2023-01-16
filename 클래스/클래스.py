class BreadMold :
    category = "크림빵"
    def make_bread() :
        print("뱅뱅뱅")
    pass

bread = BreadMold() # 객체화
bread.price = 3000

# print(bread.category, bread.price)
bread.make_bread() # 에러 발생 bread라는 객체화할경우 bread라는 인자가 
# 클래스에 전달해진다 

# 해결방안 def make_bread(self) self 대입

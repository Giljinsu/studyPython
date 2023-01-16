#__init__ 생성자 메서드
#__del__ 소멸자 메서드

class BreadMold :
    category = "빵"

    def __init__(self, price, category) : # 객체생성시 실행
        self.price = price
        self.category = category
        print("빵을 만들었습니다")

    # def __str__(self) : #
    #     return ("{}의 가격은 {}원 입니다.".format(bread1.category, bread1.price))

    def __del__(self) :
        print("빵이 사라짐")

bread1 = BreadMold(3000, "빵") # 3000원이라는 매개변수 로인해 price는 3000이 됨
# bread2 = BreadMold(2500)
# bread3 = BreadMold(2000)

# print("{}의 가격은 {}원 입니다.".format(bread1.category, bread1.price))
print(bread1) # __str__이 없으면 객체의 위치를 나타내는것이 나타남 있으면 그안에 내용이 사용됨


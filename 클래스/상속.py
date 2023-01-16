# super 부모
# sub 자식

class Parent:
    price = 15000
    def __init__(self, name , menu, recipe) :
        self.name =name
        self.menu = menu
        self.recipe = recipe
    
    def __str__(self):
        return "가게 이름 : {}, 가게의 메뉴 {}, 메뉴의 조리법{}".format(self.name,self.menu, self.recipe)
    
    def __del__(self):
        pass

class Child(Parent) :
    price = 20000 # 오버라이드 재정의
    #marketing = "온라인 마케팅" # 새로운 속성 자식 클래스 고유 속성
    def __init__(self, name, menu, recipe, marketing) :
        Parent.__init__(self,name, menu, recipe)
        self.marketing = marketing
    
    def __str__(self):
        return super().__str__() + "마케팅 방법 {}".format(self.marketing)
        # super() 상속
info = Child("자식의 가게", "붕어빵", "붕어빵을 굽는다","온라인")
print(info)
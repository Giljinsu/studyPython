menu = {"아이스 아메리카노" : 3000, "아메리카노" : 2500, "아이스 라떼":4000,
"라떼":3500, "아이스크림" : 8000}
icemenu = {}
hotmenu = {}
for i, j in menu.items() :
    if i[0:3] == "아이스" : # "아이스" in i 도 가능
        icemenu[i] = j
    else :
        hotmenu[i] = j
print("차가운메뉴")
for i , j in icemenu.items() :
    print("제품명 : {}, 가격 : {}".format(i,j))
print("뜨거운메뉴")
for i , j in hotmenu.items() :
    print("제품명 : {}, 가격 : {}".format(i,j))

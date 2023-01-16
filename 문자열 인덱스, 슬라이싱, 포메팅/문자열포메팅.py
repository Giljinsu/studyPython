weather= "맑음"
temperature = 10
chance_shower= 33.3

print("오늘의 날씨는", weather, "기온은", temperature ,"도 입니다")
print("오늘의 날씨는 %s 기온은 %d도 입니다"%(weather, temperature))

print("오늘의 날씨는 %s 기온은 %d도 비가 내릴 확률은 %.1f%%입니다"%(weather, temperature, chance_shower))

# 포메함수 어떤type이 올지 모를때 사용하면 좋다.
print("오늘의 날씨는 {} 기온은 {}도 입니다".format(weather,temperature))
#{} 안에 숫자를 놓게 되면 순서를 지정할수 있다.

#{}안에 자리를 지정줄수있다
print("오늘의 날씨는 {:10} 기온은 {:10}도 입니다".format(weather,temperature))

#{}안에 데이터 타입을 설정 가능하다
print("{0:}, {1:d}, {1:f}, {1:o}, {1:x}".format(weather,temperature))

# 정렬
left = "left"
right = "right"
middle = "middle"

# <>^ 
print("({:>10s}), ({:<10s}), ({:^10s})".format(left, right, middle))

#공백에 문자 채울수있음
print("({:!>10s}), ({:@<10s}), ({:#^10s})".format(left, right, middle))

#자릿수 정하기
print("({2:!>10.4s}), ({1:@<10.3s}), ({0:#^10.2s})".format(left, right, middle))

# f-string 간단함

print(f"오늘의 날씨는 {weather}이며 기온은 {temperature}입니다")
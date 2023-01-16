def division() :
    try :
        num1 = int(input("첫번째 정수를 입력해주세요 >>"))
        num2 = int(input("두번째 정수를 입력해주세요 >>"))

        return print("나누기 값은 {} 입니다.".format(num1/num2))
    except Exception as e: # 모든 오류 포함 KeyboardInterrupt는 미 포함
    # 모두 포함시킬려면 BaseException 사용
        print(e)
    # except ValueError # value에러만 포함
    # else : 
    #     print("정상적으로 나누기 함수가 호출 되었습니다") # return문 때문에 실행 x
    finally : # return 후 실행됨0
        print("정상 출력")
division()

# valueerror, zerodivisionError, KeyboardInterrupt
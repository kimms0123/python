from coffee import Coffee

coffeeList = [Coffee("아메리카노", 2000), Coffee("라떼", 3000), Coffee("바닐라 라떼", 3500)]
while True:
    codeNum = int(input("1. 커피 판매 2. 커피 추가 3. 프로그램 종료>>"))

    # 커피 판매
    if codeNum == 1:
        for x in coffeeList:
            print(x.intro())
        coffeeNum = int(input("번호 입력>>"))

    # 메뉴 추가
    elif codeNum == 2:
        newCoffeeName = input("커피 이름>>")
        newCoffeePrice = int(input("커피 가격>>"))
        coffeeList.append(Coffee(newCoffeeName, newCoffeePrice))
        print(f"{Coffee(newCoffeeName, newCoffeePrice)}추가 완료")

    # 프로그램 종료
    elif codeNum == 3:
        print("프로그램 종료")
        break

    # 오류
    else:
        print("프로그램 오류")
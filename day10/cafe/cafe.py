# 카페 직원용 프로그램 개발 요청
# 기능 요구 사항
# 1. 커피 판매: 판매 커피 선택
# 2. 커피 메뉴 추가: 커피 이름( 가격 )


coffeeList = [{"name": "아메리카노", "price": 2000}, {"name": "라떼", "price": 2500}, {"name": "바닐라 라떼", "price": 3000}]
while True:
    codeNum = int(input("1. 커피 판매 2. 커피 추가 3. 프로그램 종료>>"))

    # 커피 판매
    if codeNum == 1:
        for index, item in enumerate(coffeeList):
            print(f"{index}. {item['name']} {item['price']}원")
        coffeeNum = int(input("번호 입력>>"))
        print("판매 완료")

    # 메뉴 추가
    elif codeNum == 2:
        newCoffeeName = input("커피 이름>>")
        newCoffeePrice = int(input("커피 가격>>"))
        newCoffeeMenu = {"name": newCoffeeName, "price": newCoffeePrice}
        coffeeList.append(newCoffeeMenu)
        print(f"{newCoffeeMenu}추가 완료")

    # 프로그램 종료
    elif codeNum == 3:
        print("프로그램 종료")
        break

    # 오류
    else:
        print("프로그램 오류")
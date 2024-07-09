'''
# 상품의 가격과 등급을 입력받아 처리하는 함수 만드시오
# 상품 가격 등급 표
price grade
2500   'v'
96900  's'
124000 'g'
3. 입력 받은 가격과 등급을 함수의 매개변수로 전달하여/ 해당 구매 여부 판단 후 잔돈 출력
    만약 존재하지 않는 등급이면 '존재하지 않는 등급입니다' 출력
    금액이 부족할 시 '금액이 부족합니다' 출력
    매개변수의 등급도 일치하고 매개변수의 가격도 부족하지 않으면 잔돈 출력

ex)) 3000, 'v'  ----> 잔돈 500원
     90000, 's'  ----> 금액이 부족합니다
'''

'''
def change(price, grade):
    if grade == 'V' and price > 2500:
        result = price - 2500
        print(f"잔돈은 {result}원 입니다")
    elif price > 2500 and grade != 'V':
        print("존재하지 않는 등급입니다.")
    elif grade == 'V' and price < 2500:
        print("금액이 부족합니다")
    # S 등급
    if grade == 'S' and price > 96900:
        result = price - 96900
        print(f"잔돈은 {result}원 입니다")
    elif price > 2500 and grade != 'S':
        print("존재하지 않는 등급입니다.")
    elif grade == 'S' and price < 96900:
        print("금액이 부족합니다")
    # G 등급
    if grade == 'S' and price > 124000:
        result = price - 124000
        print(f"잔돈은 {result}원 입니다")
    elif price > 124000 and grade != 'S':
        print("존재하지 않는 등급입니다.")
    elif grade == 'S' and price < 124000:
        print("금액이 부족합니다")
    

a = change(3000,'V')
'''

# 함수 정의
def method1 (price, grade):
    if grade == 'V':
        if price >=2500:
            return price - 2500
    elif grade == 'S':
        if price >=96900:
            return price - 96900
    elif grade == 'G':
        if price >=124000:
            return f'잔돈은 {price - 124000}입니다.'
    else:
        return "존재하지 않는 등급입니다."


    # if를 만났는데 if랑 조건이 부합하지 않으면 그 if문을 탈출해서 아래 return을 만나서 아래 내용을 출력함
    return "금액이 부족합니다." # 조교님 질문

# 함수 호출
'''
result1 = method1(3000,'V')
print(result1)

result2 = method1(90000, 'S')
print(result2)

result3 = method1(90000, 'C')
print(result3)
'''
# 입력 받을 시
while True:
    price = int(input("금액 입력>>"))
    grade = input("등급 입력>>")

    result = method1(price,grade)
    print(result)
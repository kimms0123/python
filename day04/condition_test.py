#1. 정수를 입력받고, 양의 홀수, 양의 짝수, 0, 음의 홀수, 음의 짝수를 판별하는 프로그램
# -5 => 음의 홀수, 0=> 0
# num = int(input("정수 입력>>"))

#if-elif-else문
# if num % 2 ==0 and num > 0:
#     print("양의 짝수입니다")
# elif num % 2 ==0 and num < 0:
#     print("음의 짝수입니다.")
# elif num % 2 !=0 and num > 0:
#     print("양의 홀수입니다.")
# else:
#     print("음의 홀수입니다.")

#이중 if문
# if num % 2 == 0:
#     if num > 0:
#         print("양의 짝수입니다.")
#     else:
#         print("음의 짝수입니다.")
# elif num % 2 != 0:
#     if num > 0:
#         print("양의 홀수입니다.")
#     else:
#         print("음의 홀수입니다.")
# else:
#     print("0입니다.")

#가독성 높인 코드
# isPositive = num > 0
# isNegative = num < 0
# isOdd = num % 2 == 1
# isEven = num % 2 == 0
#
# if isPositive and isOdd:
#     print("양의 홀수입니다")
# elif isPositive and isEven:
#     print("양의 짝수입니다")
# elif isNegative and isOdd:
#     print("음의 홀수입니다.")
# elif isNegative and isEven:
#     print("음의 짝수입니다.")
# else:
#     print("0입니다.")

#2. 좌표 평면에서 위치 판별 프로그램
#사용자로부터 x축과 y축의 좌표값 x와 y를 입력받아, 해당 좌표가 좌표 평면의 어느 사분면에 위치하는지 판별하는 프로그램
#사분면에 위치하는 경우 "입력하신 좌표는 제 1사분면에 위치합니다." 등과 같이 출력하고 축 위에 있는 경우 x축 위에 위치합니다, 원점에 위치합니다등으로 출력
x = int(input("x값을 입력해주세요>>"))
y = int(input("y값을 입력해주세요>>"))

isPositive = x > 0
isNegative = x < 0
isZero = x == 0
isYPositive = y > 0
isYnegative = y < 0
isYZero = y == 0

if isZero and isYZero:
    print("원점입니다")
elif isYZero:
    print("x축 위에 위치합니다")
elif isYZero:
    print("Y축 위에 위치합니다")
elif isPositive and isYPositive:
    print("제 2사분면에 위치합니다")
elif isPositive and isYnegative:
    print("제 4사분면에 위치합니다.")
elif isNegative and isYPositive:
    print("제 1사분면에 위치합니다.")
elif isNegative and isYnegative:
    print("제 3사분면에 위치합니다.")

#3. 마트 할인 적용 프로그램
#사용자로부터 마트에서 구매한 총 금액을 입력받아, 그 금액에 따라 할인율을 적용하는 프로그램
#구매 금액 50.000원 이상이면 5% 100.000원 이상이면 10% 200.000원 이상이면 20%의 할인을 적용
#구매 금액은 {원본금액}원, 할인율은 {할인율}%, 할인 금액은 {할인금액}우너, 최종 결제 금액은 {최종 결제 금액}원입니다.
cash = int(input("구매한 금액을 입력해주세요>>"))

if cash >= 200000:
    print(f"구매 금액은 {cash}, 할인 금액은 5%, 최종 결제 금액은 {cash - cash * 0.2}원입니다.")
elif cash >= 100000:
    print(f"구매 금액은 {cash}, 할인 금액은 10%, 최종 결제 금액은 {cash - cash * 0.1}원입니다.")
elif cash >= 50000:
    print(f"구매 금액은 {cash}, 할인 금액은 5%, 최종 결제 금액은 {cash - cash * 0.05}원입니다.")

else:
    print("적용되는 할인이 없습니다.")
#while

# x = 10
#
# while x > 0:
#     print("불금인데 학원온거 ㅇㅈ")
#     x -= 1

# x = -1
# while x != 0:
#     x = int(input("숫자 0을 넣어야 멈춤>>"))

# while True:
#     x = int(input("숫자 0을 넣어야 멈춤>>"))
#     if x == 0:
#         break

# 숫자 1을 넣으면 아이스아메리카노
# 숫자 2를 넣으면 아이스 라떼
# while True:
#     x = int(input("숫자를 입력해주세요(0을 넣으면 멈춤)>>"))
#     if x == 0:
#         break
#     elif x == 1:
#         print("아이스아메리카노")
#     elif x == 2:
#         print("아이스 라떼")

#유저에게 언어를 고르세요
# 1.파이썬
# 2.자바
# 3.c++
# 4.프로그램 종료
# 그외. 숫자 잘못 입력하셨습니다.

# while True:
#     x = int(input("언어를 고르세요(1. python 2. java 3. c++ 4. 프로그램 종료>>"))
#     if x == 1:
#         print("python")
#     elif x == 2:
#         print("java")
#     elif x == 3:
#         print("c++")
#     elif x == 4:
#         print("프로그램 종료")
#         break
#     else:
#         print("숫자를 잘못 입력하셨습니다.")

# 계산기 프로그램
# 유저에게 1. 더하기 2. 빼기 3. 곱하기 4. 나누기(몫)
# 1 -> 두 정수를 입력하고, 더한 결과값이 나옴

while True:
    print("계산기 프로그램")
    num1 = int(input("정수 1을 입력해주세요>>"))
    num2 = int(input("정수 2를 입력해주세요>>"))
    x = int(input("0. 프로그램 종료 1. 더하기 2. 빼기 3. 곱하기 4. 제곱 5. 나누기(몫)>>"))

    plus = num1 + num2
    minus = num1 - num2
    multi = num1 * num2
    divide = num1 // num2
    multiMulti = num1 ** num2

    if x == 0:
        print("프로그램 종료")
        break
    elif x == 1:
        print(plus)
    elif x == 2:
        print(minus)
    elif x == 3:
        print(multi)
    elif x == 4:
        print(multiMulti)
    elif x == 5:
        print(divide)
    else:
        print("입력 오류")

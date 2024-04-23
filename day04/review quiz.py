#1. 정수 평균 계산 프로그램
#사용자로부터 3개의 정수를 입력받아 평균을 계산하라.
num1 = int(input("정수1을 입력해주세요>>"))
num2 = int(input("정수2를 입력해주세요>>"))
num3 = int(input("정수3을 입력해주세요>>"))

ave = (num1+num2+num3)/3

print(f"평균은 {ave}입니다.")

#2. 가장 큰 정수 찾기 프로그램
# 사용자로부터 3개의 정수 [숫자 모드 다름}을 입력받아 가장 큰 정수를 출력하세요.
num1 = int(input("정수 1을 입력해주세요>>"))
num2 = int(input("정수 2를 입력해주세요>>"))
num3 = int(input("정수 3을 입력해주세요>>"))

num1Max = num1 > num2 and num1 > num3
num2Max = num2 > num1 and num2 > num3

if num1Max:
    print(f"가장 큰 숫자는 {num1}")
elif num2Max:
    print(f"가장 큰 숫자는 {num2}")
else:
    print(f"가장 큰 숫자는 {num3}")

#3. 입력한 정수의 배수 출력 프로그램
# 사용자로부터 정수를 입력받아, 해당 정수의 배수를 100까지 출력하세요
num = int(input("정수를 입력해주세요>>"))

for x in range (101):
    if x % num == 0:
        print(x)

for x in range(5,70):
    print(x)

for x in "koreaIT":
    print(x)


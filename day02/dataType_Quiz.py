#Q. 유저에게 첫 번째 정수와 두 번째 정수를 입력 받은 후 두 수의 합을 출력하는 프로그램
#출력 예시: 첫 번째 정수 : 5
# 두 번째 정수: 3
# 결과: 8
num1 = int(input("정수1을 입력해주세요>>"))
num2 = int(input("정수2를 입력해주세요>>"))
result = num1 + num2

print(f"결과: {result}")

#강사님 답
num1 = input("정수1을 입력해주세요>>")
num2 = input("정수2를 입력해주세요>>")
result = int(num1) + int(num2)

print(f"결과: {result}")

#Q2. 나이를 통한 출생년도 알아내기
age = input("나이를 입력해주세요>>")
year = 2024 - int(age) +1

print(f"나이가 {age}살이라면, 출생년도는 {year}입니다.")
#강사님 답
#year = 2024 - int(age) +1

#Q3. 정사각형 넓이 계산 프로그램
side = input("한 변의 길이를 입력해주세요>>")
width = int(side) * int(side)

print(f"한 변의 길이가 {side}cm 라면, 넓이는 {width}cm^2입니다.")

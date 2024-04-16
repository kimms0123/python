# 1. 원화 변환기
# 현재 원화를 입력 하면 달러로 바뀌는 프로그램을 작성
# 예시)) 1410 - 1$

won = int(input("현재 원화를 입력해주세요>>"))
dallor = won / 1410
print(f"{won} = {dallor}$")

# 2. 수학 연산 프로그램
# 사용자로부터 두개의 숫자를 입력받아 이 두 숫자에 대한 합, 차, 곱, 목, 나머지, 제곱을 계산하는 프로그램을 작성하라
# 입력받은 두 숫자에 대해 다음 괕은 연산결과를 출력해주는 프로그램
# 사용자 입력
# 예시 정수 )) 12, 3

num1 = int(input("정수 1를 입력해주세요>>"))
num2 = int(input("정수 2를 입력해주세요>>"))

hap = num1 + num2
minus = num1 - num2
gop = num1*num2
divide = num1 // num2
other = num1 % num2
jegop = num1 ** num2

print(f"합: {hap} 빼기: {minus} 곱: {gop} 몫:{divide} 나머지: {other} 제곱: {jegop}")

# 3. 원의 둘레와 넓이 계산 프로그램
# 사용자로부터 원의 반지름을 입력받아, 그 우너의 둘레와 넓이를 계산하는 프로그램
# 원의 둘레는 2*파이* 반지름
# 원의 넓이: 파이* 반지름^2
# 예시 정수)) 5

circle = int(input("원의 반지름을 입력해주세요>>"))
circlelen = 2 * 3.14 * circle
circlewidth = 3.14 * circle**2

print(f"원의 둘레: {circlelen}")
print(f"원의 넓이: {circlewidth}")
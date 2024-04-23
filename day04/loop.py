# 반복문 (loop)
# for 반복문

# for 미지수 in range (n번):
# range(n): 0~n-1까지 순회
# for i in range(10):
#     print(f"{i}. Hello World!")

# num = int(input("몇 번 실행하는가>>"))
#
# for x in range(num):
#     print(f"{x}. Hello World")

# 1. 0~200까지 찍는 프로그램
# for x in range (201):
#     print(f"{x}")

# 2. 0~200까지 짝수만 찍는 프로그램

# for x in range(101):
#     if x % 2 == 0:
#         print(x)

# 3. 0~1000까지 3의 배수만 찍는 프로그램
# for x in range(1001):
#     if x % 3 == 0:
#         print(x)

# 4. 구구단 프로그램
# 사용자에게 몇 단을 입력받으면 해당 단을 출력하는 프로그램
dan = int(input("단을 입력하시오>>"))

for x in range(10):
    print(f"{dan} x {x} = {dan*x}")
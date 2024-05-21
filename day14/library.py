import math # 수학적 기능
import random # 숫자 랜덤 출력

# print(random.randint(0, 10000))

# 랜덤으로 6개의 숫자를 뽑아주는 프로그램 [1~45] 중복 x
lotto = []

while True:
    num = random.randint(1, 45)
    if lotto.count(num) == 0:
        lotto.append(num)
        if len(lotto) == 6:
            break

lotto.sort()
# print(lotto)

# print(random.choice(["사과", "바나나", "키위"]))

# 유저가 6개 번호를 입력하고 몇 등인지 알려주는 프로그램
choice = [int(input(f"{x}. 번호 입력:")) for x in range(6)]
rank = 6

for x in lotto:
    if choice.count(x) > 0:
        rank -= 1
print(f"로또: {lotto}")
print(f"당신: {choice}")
print(f"{rank}등 축하드립니다")


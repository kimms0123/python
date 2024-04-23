# 1. 유저에게 다섯개의 변수를 입력받고, 리스트화한 다음 각각 요소를 3배로 만든 다음 출력
# ex [6, 1, 2, 5, 19] => [15, 3, 6, 15, 57]
numList = []

for x in range(5):
    num = int(input("정수 입력>>"))
    numList.append(num)
print(numList)

# 각 요소 3배 만들기
newNumList = []

newNumList.append()
print(newNumList)

# 강사님 답
numList = []

for x in range(5):
    num = int(input("정수 입력>>"))
    numList.append(num)

newNumList = []

for x in numList:
    print(x*3)
    newNumList.append(x*3)
print(newNumList)

# 2. 유저에게 서로 다른 다섯개의 정수를 입력 받고, 리스트화 한 다음, 가장 큰 수를 뽑아내는 프로그램
numList = []

for x in range(5):
    num = int(input("정수 입력>>"))
    numList.append(num)
numList.sort()
numList.reverse()
print(numList[0])


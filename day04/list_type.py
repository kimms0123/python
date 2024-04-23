# 어떠한 타입. 그 관련된 기능

# list_type
# soccerPlayer = ["손흥민", "황희찬", "김민재", "이강인"]
# print(soccerPlayer[2]) # 김민재
#
# soccerPlayer.append("이재성") # 리스트 추가 함수
# print(soccerPlayer) # ["손흥민", "황희찬", "김민재", "이강인", "이재성"]
# soccerPlayer.sort()# 리스트 정렬 함수
# print(soccerPlayer)

# 1. 유저에게 과일을 영어로 3개 입력 받고 과일 리스트를 만들고, 오름차순으로 보여주기
# a = input("과일 입력>>")
# upperA = a.upper()
# b = input("과일 입력>>")
# upperB = b.upper()
# c = input("과일 입력>>")
# upperC= c.upper()
#
# fruit = []
# fruit.append(upperA)
# fruit.append(upperB)
# fruit.append(upperC)
# print(fruit)

# 코드 정리
fruitList = []

for x in range(3):
    fruit = input("과일 입력>>")
    fruitList.append(fruit.upper())
    fruitList.sort()
    print(fruitList)
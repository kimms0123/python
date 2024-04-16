#인덱싱
#멤버쉽 연산자 [in]
coffee = "americano"
print('a' in coffee) #True
print('ameri' in coffee) #True

text = """""" # 두 문자 이상의 글
news = """메이저리그 샌디에이고의 김하성이 안타와 볼넷으로 3번 출루하며 팀의 역전승에 힘을 보탰습니다.
김하성은 밀워키와 원정경기에 6번 타자 유격수로 선발 출전해 1회 좌전 안타에 이어 5회와 7회 볼넷을 얻어냈습니다.
타점과 득점도 하나씩 올린 김하성의 활약으로 샌디에이고는 밀워키에 7대 3 역전승을 거뒀습니다."""
print("메이저리그" in news) #True

#슬라이싱 [:]
car = "tesla"
print(car[0:3]) #tes
print(car[1:3]) #es

#인덱싱 연산자
code = "python"
print(code[0]) #p
print(code[3]) #h


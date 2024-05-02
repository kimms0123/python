# map(how, target): target을 바꿔 주기
numList = [x for x in range(101)]

result = list(map(lambda x: x+100, numList)) # list화 시켜 줘야함
print(result)

emailList = ["abc@naver.com", "mega@gmail.com", "korea@daum.net"]
# map -> 유저아이디로 바꾸기
result_1 = list(map(lambda x: x.split("@")[0], emailList))

#filter: target을 필터링해줌
result1 = list(filter(lambda x: x % 2 == 0, numList))
print(result1)

fruits = ["apple", "banana", "cherry", "kiwi"]

# fruits에서 5글자 이하인 애들만 살리기
result2 = list(filter(lambda x: len(x) <= 5, fruits))
print(result2)

# 알파벳 a가 포함 되어 있는 단어 살리기
result3 = list(filter(lambda x: "a" in x, fruits))
print(result3)


# 제일 작은 수 제거하기
# 정수를 저장한 배열 arr에서 가장 작은 수를 제거한 배열을 리턴하는 함수 solution을 완성
# 단, 리턴하는 배열이 빈 배열인 경우 -1을 채워 리턴해라
def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(min(arr))
        return arr

# 문자열 섞기
def solution1(str1, str2):
    text = ""
    for x in range(len(str1)):
        text += str1[x]
        text += str2[x]
    return text

print(solution1("aaaa","ababab"))

# x 사이의 개수
# 문자열 myString이 주어집니다. 이를 문자 x 기준으로 나눴을 때 나눠진 문자열 각각의 길이를 순서대로 저장한 배열을
# return하는 함수
def solution2(myString):
    b = ()
    c = list(map(lambda x: len(x), (filter(lambda x: len(x) > 0, myString))))
    return c

# 5명씩
arr = ["kim", "lee", "han", "kang", "young","park"]
def solution3(arr):
    return [item for index, item in enumerate(arr) if index % 5 == 0]


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "~소리 내는중~"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{super().speak()} ... 멍멍"

a = Dog("max","siba")
print(a.speak())
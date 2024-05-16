# 1. 문자열 뒤집기
# 문자열 my_string이 매개변수로 주어짐, my_string을 거꾸로 뒤집은 문자열을 return하도록 함수를 완성해라
# def reversedWord(my_string):
#     wordList = list(my_string)
#     wordList.reverse()
#     reversedWord = "".join(wordList)
#     return reversedWord
#
# print(reversedWord("hello"))
#
# # 2. True인 애들만 리스트화 해서 돌려주기
# def filterDoneList(todoList, doneList):
#     [item for index, item in enumerate(todoList) if doneList[index] == True]

class animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def eat(self):
        print("냠냠")

    def sound(self):
        pass

    def intro(self):
        return f"제 이름은 {self.name}이고, {self.breed}(종) 입니다."

class Dog(animal):
    def sound(self):
        print("멍멍")

class Cat(animal):
    def sound(self):
        print("냐옿")

# 퀴즈
# 관리자, 편집자, 뷰어라는 각각 사용자가 존재
# 모두 '접근하기'라는 함수를 지님, username이라는 속성 지님.

# 관리자 - 유저 만들기
# 편집자 - 편집하기
# 뷰어 - 조회하기

class User:
    def __init__(self, userName):
        self.userName = userName

    def acceess(self):
        pass

class Admin(User):
    def acceess(self):
        print("관리자가 접근합니다")

    def makeUser(self):
        print("유저 생성 완료")

class Edit(User):
    def acceess(self):
        print("편집자가 접근합니다")

    def editing(self):
        print("편집 완료")

class Viewer(User):
    def acceess(self):
        print("뷰어가 접근합니다")

    def check(self):
        print("조회 실행")

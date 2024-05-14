class Dog:
    # 생성 해주는 친구(생성자): init
    def __init__(self, a, b):
        self.name = a
        self.breed = b

    def barking(self):
        print("멍멍")

a = Dog("월트", "달마시안")
a.barking()


# book 클래스 만들기
# 제목, 작가를 가지는 클래스
class Book:
    def __init__(self, tilte, author):
        self.title = tilte
        self.author = author
    # display_info: 문자열로 책 제목:{} 작가:{}
    def display_info(self):
        return f"책 제목:{self.title} 작가:{self.author}"
    def find(self):
        self.display_info()


b = Book("데미안","헤르만 헤세")
print(b.display_info())











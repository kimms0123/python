class Dog:
    # 변수들
    def __init__(self, a, b):
        self.name = a
        self.breed = b
        self.happiness = 0

    # 함수들
    def intro(self):
        print(f"{self.name} {self.breed} {self.happiness}")

    def eating(self):
        print("밥 먹는다")
        self.happiness += 10

a = Dog("제니", "푸들")
a.intro()
b = Dog("맥스", "달마시안")
b.intro()
c = Dog("누렁이", "시바")
c.intro()
class Animal:
    def eating(self):
        print("냠냠녕녕뇸뇸")

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("멍멍")

class Cat(Animal):
    def speak(self):
        print("오왜랃망뢈ㅇ")

a = Dog()
a.eating()
a.speak()

b = Cat()
b.eating()
b.speak()
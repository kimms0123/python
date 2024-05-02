# x: 1, "hello", [], {}, ···
# x: 함수도 들어갈 수 있음(합성 함수)
# f(g(x))
def a(x):
    print("a함수 실행")
    x() # x 함수화
def b():
    print("b함수 실행")

print(a(b)) # a함수 실행 후 x의 매개변수에 b()함수 가 들어가 b 함수 실행

# 게임 몬스터 프로그램
def killing_monster(monster, event):
    print(f"{monster}를 처치했습니다!")
    event()

def getGold():
    print("골드 획득!")
def getFood():
    print("음식 획득!")

killing_monster("슬라임",getGold)
killing_monster("늑대",getFood)


# 태어난 년도로 띠 알아보기
# 년도 입력, 그에 해당하는 띠를 알려주는 함수
# 띠: 자(子), 축(丑), 인(寅), 묘(卯), 진(辰), 사(巳), 오(午), 미(未), 신(申), 유(酉), 술(戌)
def yearToZodiac(year):
    zodiac = {
        0: "원숭이",
        1: "닭",
        2: "개",
        3: "돼지",
        4: "소",
        5: "쥐",
        6: "호랑이",
        7: "토끼",
        8: "용",
        9: "뱀",
        10: "말",
        11: "양",

    }

    return zodiac[year % 12]
print(yearToZodiac(2003))

# 숫자 뒤집기
# n을 뒤집어 각 자리의 숫자를 원소로 가지는 배열 형태를 돌려주는 함수 ex) n = 1234 -> 4321
def reverseNum(num):
    numList = list(num)
    numList.reverse()
    reverseNumList = "".join(numList)
    return list(reverseNumList)
print(reverseNum("12345"))

def makeReverseList(x):
    a = list(str(x))
    a.reverse()
    b = list(map(lambda x:int(x), a))
    return b
def makeReversedNum(x):
    return list(map(lambda x: int(x),reversed(list(str(x)))))

print(makeReverseList(12345))
print(makeReversedNum(12345))

# 짝수는 싫어요
# n이 매개변수로 주어질 시 n이하의 홀수가 오름차순으로 담긴 배열 리턴 함수 ex) n = 10 -> [1, 3, 5, 7, 9]
def solution(num):
    return [x for x in range(num+1) if x % 2 == 1]

print(solution(10))

# random 사용해서 띠함수를 사용하여 100개 띠들이 있는 리스트 만들기
import random

a = [yearToZodiac(random.randint(1930,2025)) for x in range(100)]
print(a)

# random.randint(0, 100)
# random.choice(["콜라", "사이다", "환타", "스프라이트"])
# random.shuffle(["콜라", "사이다", "환타", "스프라이트"]
# random.choices(["콜라", "사이다", "환타", "스프라이트"], [6,2,1,1], k = 1000) # (내용, 비율, 갯수)


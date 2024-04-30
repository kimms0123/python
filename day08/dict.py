# 기본 타입: a = 1, b =3.14, c = True, d = "hello"
# e = [], f = {}
person = {
    'name': "엄준식",
    'age': 22,
    'town': "동탄시",
    'coffeeList': ["아메리카노", "라떼", "민트"],
    'academy': {
        'first': "java",
        "second": "c-langauge",
        "third": "python",
    },
}

print(f"이름: {person["name"]} 동네: {person["town"]} 3번째로 좋아한는 커피: {person["coffeeList"][2]} 학원의 3번재 수업: {person["academy"]["third"]}")

# 데이터 생성
person["gender"] = "woman" # k - v 데이터 만들기

# 데이터 삭제
del person["town"]
print(person)

# dict 기능
print(person.keys()) # key들만 출력
print(person.values()) # value들만 출력
print(person.items()) # k - v 모두 출력
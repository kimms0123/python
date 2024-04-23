fruit = ["apple", "kiwi","banana"]
number = [1, 2, 3, 4, 5]
mix = ["안녕", 1, "집 보내줘", 2, []]
starbucks = [["아메리카노", "라테"], ["쥬스", "에이드"], ["빵", "케이크"]]

print(starbucks[0][1])
print(starbucks[2][0])

#append(추가하다)_그냥 추가(리스트도 그냥 추가함)
fruit.append("grape")
print(fruit)

#extend(확장하다)_리스트를 확장(리스트 안에 자리를 늘려서 추가해줌)
fruit.extend(["strawberry","orange"])
print(fruit)

#sort(정렬하다)
fruit.sort()
print(fruit)

#reverse(반대로 정렬하다)
fruit.reverse()
print(fruit)

#pop(튀다)_리스트 맨 뒤 없애기
fruit.pop()
print(fruit)

#remove(제거하다)
fruit.remove("orange")
print(fruit)

#count(세다)
x = fruit.count("banana")
print(x)

# for 리스트는 요소를 하나씩 출력한다.
for x in fruit:
    print(x)
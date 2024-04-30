# [0~100]리스트 출력
list = []

for x in range(101):
    list.append(x)
print(list)

# [0~100]리스트 출력 간략화
a = [x for x in range(101)]
print(a)

# "apple" => [a,p,p,l,e]
b = [x for x in "apple"]
print(b)


# filtering Comprehension
# [0 ~ 10]까지 짝수 리스트 출력
c = [x for x in range(11) if x % 2 == 0]
print(c)

# [0 ~ 100]까지 홀수 리스트 출력
d = [x for x in range(101) if x % 2 != 0]
print(d)

# [0 ~ 100]까지 짝수를 제곱인 형태인 리스트
e = [x**2 for x in range(101) if x % 2 == 0]
print(e)

# [0 ~ 10] 홀수를 10을 더한 리스트
f = [x+10 for x in range(11) if x % 2 != 0]
print(f)

# fruits => [5, 6, 4, 5, 6]
fruits = ["apple", "banana", "kiwi", "grape", "orange"]
g = [len(x) for x in fruits]
print(g)

# i가 포함되어 있으면 길이로 변환
fruits = ["apple", "banana", "kiwi", "grape", "orange"]
h = [len(x) for x in fruits if "i" in x]
print(h)


# 매핑 comprehension
# [0 ~ 10]까지 홀수이면 10을 더하고 짝수이면 20을 더한 리스트
i = [x + 10 if x % 2 != 0 else x + 20 for x in range(101)]
print(i)

# 5 글자 이하이면 글자의 길이로 나타내고, 아니면 대문자화 하기
fruits = ["apple", "banana", "kiwi", "grape", "orange"]
j = [len(x) if len(x) <= 5 else x.upper() for x in fruits]
print(j)

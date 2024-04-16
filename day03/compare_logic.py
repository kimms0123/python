#compare_logic.py [비교 연산자]
# >, <, <=, >=, ==, !=
a = 10
b = 20

print(a > b) #초과 false
print(a >= b) #이상 false
print(a < b) #미만 ture
print(a <= b) #이하 ture
print(a == b) #동등 false
print(a != b) #비동등  ture

#logic(논리) 연산자
# and, or, not
c = 5
d = 3

#and: 모든 조건이 참이면 참
print(c > d and c == 5 and d== 3) #True

#or: 하나라도 조건이 참이면 참
print(c < d or c == 6 or d == 3) #True

#not: 조건의 반대를 반환
print(not(c > d)) #False

#프로그래밍에 수학적 능력이 필요한 이유
x =5
result = x > 3 and x == 5 # True
#드모르간 법칙 적용
result1 = not(x <= 3) or not(x != 5) #True
# 변수: RAM에 저장 하는 공간
# 2+3 = 5 인간: 연산 + 기억[뇌]
# 2+3 = 5 컴퓨터: 연산[CPU] +기억[RAM] (폰노이만 구조)
# a = 2 + 5 [숫자]
# a = "안녕하세요" [문자]
# 데이터 타입

#데이터 타입의 종류
a1= 1 #정수형 타입
a2 = 3.14 #실수형 타입
a3 = "안녕" #문자형 타입
a4 = True #불리언형 타입 [yes or no]
a5 = False #불리언형 타입 [yes or no]
a6 = None #None형 타입 [없음]

#정수형, 실수형 타입
#사칙연산이 적용
b = 2 + 3.14

#문자형 타입
#연결 연산
c = "300" + "200"
#반복 연산
c1 = "300" * 5

#type(): 타입을 알려주는 기능
print(type(1))
print(type("1"))
print(type(True))
print(type(None))

#type-casting [타입 변환]
#정수화: int()
i = int("100")
i1 = int(3.24)
print(i)
print(i1)

#실수화: float()
f = float("3.14")
print (f)

#문자화: str()
s = str(True)
s1 = str(3.14)
print(s)
print(s1)

#불리언: bool()
bool()# True[앵간하면 전부 true] or False[0,"",none]
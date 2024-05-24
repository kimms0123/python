# 조건에 맞게 수열 변환
# 배열 arr&자연수k가 주어짐 k가 홀수라면 모든 원소에 k곱하고 k가 짝수면 모든 원소에 k를 더함 arr리턴하는 함수
def solution(arr, k):
    newArr = []
    if k % 2 == 1:
        for x in arr:
            newArr.append(x * k)
    else:
        for x in arr:
            newArr.append(x + k)
    return newArr
print(solution([1, 2, 3, 4, 5], 2))
# 문제: arr을 반환하는 것이 아님

def solution_1(arr,k):
    return [x * k if k % 2 == 1 else x + k for x in arr]

print(solution_1([1, 2, 3, 4, 5], 3))

# A강조하기
# 문자열 myString이 주어지고 myString에서 알파벳 "a"가 등장하면 전부 "A"로 변환하고 나머지 대무낮 알파벳은 소문자 알파벳으로 변환
def solution1(myString):
    return "".join(['A' if x == 'a' else x.lower() for x in myString])

print(solution1("adfegsdaewaafdsasdfa"))

# 오늘 날짜 05-24, 05-25... 06-24까지 담긴 리스트
import datetime

def solution3(x):
    today = datetime.date.today()
    futureTime = today + datetime.timedelta(days=x)
    return futureTime.strftime("%m-%d")
a = [solution3(x) for x in range(31)]
print(a)





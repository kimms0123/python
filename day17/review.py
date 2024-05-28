# 문자열 잘라서 정렬하기
# mystring 주어지고 x를 기중으로 문자열을 잘라내 배열을 만들고 사전순으로 정렬한 배열 리턴
def solution(mystring):
    filterdList = list(filter(lambda x: x != "", mystring.split("x")))
    filterdList.sort()
    return filterdList
print(solution("adxsgewxsdfex"))

# 배열 원소 삭제하기
# 정수 배열 arr과 delete_list가 잇음 arr의 원소 중 delete_list의 원소를 모두 삭제 후 남은 원소들을 기존arr있던 순서 유지한 배열 리턴
arr = [200,1000,394,65,44]
delete_list = [200,1000,44]
def solution2(arr,delete_list):
    return list(filter(lambda x: x not in delete_list, arr))

print(solution2([100,122,44,135,1000],[44,1000]))

# 최대값 만들기
# 정수 배열 numbers가 매개변수로 주어짐. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓갑을 리턴하는 함수
def solution3(numbers):
    numbers.sort()
    if numbers[0]*numbers[1] > numbers[-1]*numbers[-2]:
        return numbers[0]*numbers[1]
    else:
        return numbers[-1]*numbers[-2]

print(solution3([-1,5,6,-7,10]))









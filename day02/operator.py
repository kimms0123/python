# 100의 자리 추출기 프로그램
num = input("10,000~99,999 사이의 양의 정수를 입력해주세요>>")
intNum= int(num)
hundred = intNum // 100
result = hundred % 10

print(f"입력하신 값 {num}의 100의 자리는 {result}입니다")
#1. 정삼각형의 넓이 계산 프로그램
#사용자로부터 정삼각형의 밑변과 높이를 입력받아, 정삼각형의 넓이를 계산하는 프로그램
#정삼각형 넓이 공식: 넓이 = 밑변 * 높이 * 0.5
width = int(input("밑변을 입력해주세요>>"))
height = int(input("높이를 입력해주세요>>"))

result = int(width * height * 0.5)

print(f"정삼각형의 넓이는 {result}입니다.")

#정수의 속성 판별 프로그램
#사용자로부터 하나의 정수를 입력받아, 해당 숫자가 양수이면서 동시에 홀수인지를 판별하는 프로그램
#조건을 만족하면 '양수이며 홀수 입니다'라고 출력하고 하나라도 조건을 만족하지 않으면 '양수가 아니거나 홀수가 아닙니다' 출력
num = int(input("정수를 입력해주세요>>"))

if num % 2 != 0 and num > 0:
    print("양수이며, 홀수입니다.")
else:
    print("양수가 아니거나 홀수가 아닙니다.")

#과일 이름의 알파벳 검사 프로그램
#사용자로부터 과일의 이름을 입력받아, 해당 과일 이름에 알파벳 'a'가 포함되어 있는지를 검사하는 프로그램
#입력받은 과일 이름에 'a'가 포함되어 있다면 '해당 과일 이름에 'a'가 포함되는군요' 출력 아니면 'a'가 포함되지 않는군요' 출력
fruit = input("과일이름을 입력해주세요>>")

if 'a' in fruit or 'A' in fruit:
    print("입력하신 과일이름에 'a'가 포함되는군요.")
else:
    print("입력하신 과일이름에 'a'가 포함되지 않는군요.")
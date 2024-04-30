# 1. 문자열 문자 반복 프로그램
# 주어진 문자열 word의 각 문자를 정수 n 만큼 반복하여 새로운 문자열 생성
# word = input("단어 입력>>")
# count = int(input("반복하고 싶은 횟수를 입력하세요>>"))
#
# newWord = ""
# for x in word:
#     newWord += x * count
# print(newWord)

# 2. 모음 대문자화 프로그램
# word = input("원하는 단어 입력>>")
# gather = "aeiou"
# newWord = ""
#
# for x in word:
#     if x in gather:
#         newWord += x.upper()
#     else:
#         newWord += x
#
# print(newWord)

# 3. 대문자 -> 소문자, 소문자 -> 대문자 변환 프로그램
# word = input("단어 입력>>")
# newWord = ""
# for x in word:
#     if x.isupper():
#         newWord += x.lower()
#     else:
#         newWord += x.upper()
# print(newWord)

# 4. 단어 입력 시 자음은 대문화 해서 출력
word = input("단어 입력>>")
newWord = ""

for x in word:
    if x in "aeiou":
        newWord += x
    else:
        newWord += x.upper()
print(newWord)
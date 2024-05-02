# 이메일 주소 분리 프로그램
# 사용자로부터 전체 이메일 주소를 입력 받는다. 이메일 주소에서 사용자의 이름 부분과 도메인 부분을 분리하여 출력
# 입력: "itKorea@naver.com
# # 출력: user: itKorea domain: naver.com
# def splitEmail(email):
#     arr = email.split("@")
#     return {"user": arr[0], "domain": arr[1]}
# print(splitEmail("koreaIT@naver.com"))

# 문자열 변환 마법 퀴즈
# 사용자로부터 문자열을 받고, 입력된 문자열을 뒤집어 순서를 바꾸고, 하나는 문자열의 문자들을 알파벳 순서로 정렬한다.
# def magicStr (word):
#     # 순서대로 정렬
#     wordList = list(word)
#     list_1 = wordList.sort()
#     strspell = "".join(wordList)
#
#     # 반대로 정렬
#     wordList2 = list(word)
#     list_2 = wordList2.reverse()
#     strspell2 = "".join(wordList2)
#     return {"sorted":strspell, "reversed":strspell2}
# # 출력
# print(magicStr("mega"))

# 정수 n이 주어질 때, 홀수면 "odd" 아니면 "even"을 돌려주는 함수
def oddOrEven(x):
    # 홀수일 때
    if x % 2 != 0:
        return "odd"
    else:
        return "even"
print(oddOrEven(5))
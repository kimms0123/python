# length
# len: 문자열 또는 리스트의 길이를 알려주는 기능
print(len("hello"))
print(len("python"))
print(len([2, 4, 6, 8, 10]))

# max, min
print(max([2, 12, 3, 51, 23, 312, 3312, 1]))
print(min([2, 12, 3, 51, 23, 312, 3312, 1]))

# sum
print(sum([1, 2, 3, 4, 5]))

# 1. 영어 기사 스크랩 후, 단어 길이가 6글자 이상인 단어들만 출력하기
# news = """The weapons were sent as part of a previous US support package, and arrived this month.
# Officials said they were not announced publicly to maintain Ukraine's "operational security"."""
#
# words = news.split(" ")
# for x in words:
#     if len(x) == 6:
#         print(x)

fruits = ["apple","banana", "kiwi", "strawberry", "pineapple", "melon"]
# 2. 문자 길이가 5글자 이하이고, 알파벳 a,e가 포함되면 대문자로 출력하고,
# 그게 아니면 그 과일의 문자 길이를 출력하는 프로그램
words = ""

for x in fruits:
    if len(x) <= 5 and ("a" in x or "e" in x):
        print(x.upper())
    else:
        print(len(x))


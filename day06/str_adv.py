language = "python is a great language."

# find_위치를 알려주는 기능
a = language.find("great")
print(a)

#replace_재배치
b = language.replace("python", "java")
print(b)

#upper, lower_대문자, 소문자
c = language.upper()
d = language.lower()
print(c)
print(d)

#split(찢다)_해당 언어 기준으로 잘라 나누어라
e = language.split("is")
print(e)

#join_문자와 문자 사이에 "내용" 들어감
f = "＞︿＜".join(["hello","world"])
print(f)

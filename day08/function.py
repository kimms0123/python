# 함수: input[int, str, [], None] → output
# 마술상자: [100 → 500, 200 → 1000, 300 → ?]
# f(x) ⇒ len(x), str(x), int(x), print(x), input(x), .count(x)

def koreaIt(x):
    return x + "코리아아이티"

a = koreaIt("인천점")
print(a)

def add(x,y):
    return x+y
a = add(1,5)
print(a)

# 어떠한 단어를 넣었을 때, 그 단어가 5글자 이상이면 글자가 길어요! 아니면 글자가 짧아요! 함수
def wordLen(x):
    if len(x) >= 5:
        return "글자가 길어요!"
    else:
        return "글자가 짧아요!"
b = wordLen(input("단어 입력>>"))
print(b)

# 함수: input → [로직] → output

# abc(3, '🥚') → [🥚🥚🥚🥚🥚]
def makeEmoji(x,y):
    return [y for x in range(x)]
c = makeEmoji(3,'🥚')
print(c)

# 🥚🐣🐓🍗
# 🥚 → 🐣
# 🐣 → 🐓
# 🐓 → 🍗
def changeEmoji(x):
    if x == "🥚":
        return "🐣"
    elif x == "🐣":
        return "🐓"
    elif x == "🐓":
        return "🍗"
    else:
        return "잘못 입력하셨습니다."
print(changeEmoji('🥚'))

def changeEmoji_2(x):
    dictChange = {
        "🥚":"🐣",
        "🐣":"🐓",
        "🐓":"🍗",
    }
    return dictChange[x]
print(changeEmoji_2('🥚'))
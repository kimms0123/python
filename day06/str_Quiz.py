# 1. 뉴스 기사를 스크랩 해오고, 유저가 입력한 단어를 뉴스 기사에서 그 해당 단어를 모두 대문자화 시켜서 출력

news = """Trump Will Fight Attempts to Silence Him Before Key Witness Testifies
Justice Juan M. Merchan will hear arguments over whether the former president violated his gag order before The National Enquirer’s former publisher takes the stand."""
#유저 단어 입력
word = input("단어를 입력하세요>>")

newNews = news.replace(word, word.upper())
print(newNews)

# 2. 영어 기사를 스크랩 해오고, 단어 사이에 "🍅" 넣고 출력하기

news = """Trump Will Fight Attempts to Silence Him Before Key Witness Testifies
Justice Juan M. Merchan will hear arguments over whether the former president violated his gag order before The National Enquirer’s former publisher takes the stand."""

words = news.split(" ")
news1 = "🍅".join(words)
print(news1)
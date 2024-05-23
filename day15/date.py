import datetime

a = datetime.datetime.now()
b = datetime.datetime.now().strftime("%Y-%m-%d")
c = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

d = datetime.date.today()

# 두 날짜나 시간 사이의 기간 표기법
today = datetime.date.today()
nextWeek = today + datetime.timedelta(days=7) # 몇 일 흐른 뒤를 알려 주는 애
print(nextWeek.strftime("%y-%m-%d"))


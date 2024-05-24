# 메가커피 당일 매출 기록표
# 이름 메뉴 몇시 결제수단 포장유무
# 1000명

import pandas
from faker import Faker
import random
import datetime

mk_name = Faker('ko_KR')
pay = ["카드","현금","삼성페이", "애플페이"]
menu = ["아메리카노", "라떼", "에이드","주스","생수","에스프레소","스무디"]
take_off = ["포장","매장"]
# def get_random_time():
#     s = datetime.datetime.strftime("09:00","%H:%M")
#     e = datetime.datetime.strftime("22:00","%H:%M")
#     total = int((e-s).total_seconds() / 60) # 전체 몇분
#     random_minutes = random.randint(0, total)
#     return s + datetime.timedelta(minutes=random_minutes)
# print(get_random_time().strftime("%H:%M"))


mega_coffee = {
    'name':[mk_name.name() for x in range(1000)],
    'menu':[random.choices(menu,[3,1,2,1,1,1,1]) for x in range(1000)],
    'pay':[random.choices(pay,[3,1,3,3]) for x in range(1000)],
    'take-off':[random.choice(take_off) for x in range(1000)]
}

df = pandas.DataFrame(mega_coffee)
df.to_csv('mega-coffee-soldList.csv',index=False,encoding='cp949')

# pandas 라이브러리 설치
import pandas # 데이터 분석 라이브러리

# arr = [1 for x in range(101)]
# series = pandas.Series(arr) # 엑셀 한 열
# print(series)
#
# data = {
#     'movies':["혹성탈출", "범죄도시4", "설계자", "퓨리오사"],
#     'popcorn':["오리지널 팝콘", "어니언 팝콘", "카라멜 팝콘", "치즈 팝콘"],
#     'beverage':["콜라", "제로콜라", "사이다", "제로사이다"]
# }
#
# df = pandas.DataFrame(data) # 엑셀화 시켜줌
# print(df)
#
# # 학생 이름, 학년, 전공, 평균 학점 = 10명의 데이터를 만들어서 프레임화
# school = {
#     'name':["김철수","김양갱","전원우","안보현","김수현","김민규","이석민","이지훈","권순영","최승철"],
#     'grade':[1, 1, 2, 3, 4, 4, 2, 2, 1, 4],
#     'major':["컴퓨터공학","전기공학","프로게이머","연극영화","실용음악","실용음악","실용음악","엔터테이먼트","법학", "경행"],
#     'score':[4.0, 2.5, 4.5, 3.5, 4.1, 4.4, 3.0, 2.9, 3.6, 4.2],
# }
#
# sdf = pandas.DataFrame(school)
# print(sdf)

# 1000명
from faker import Faker
import random
import math

majorList = ["국문","수학","연영","컴공","철학","교육","법학","수의","경제","건축","경행","간호","전전","기계","물리","일문","통상무역"]
f = Faker('ko_KR')
ma = Faker('ko_KR')

school1 = {
    'name': [f.name() for x in range(1000)],
    'grade': [random.randint(1,5) for x in range(1000)],
    'major': [random.choice(majorList) for x in range(1000)],
    'score': [round(random.uniform(1, 4.5),2) for x in range(1000)]
}

sdf_2 = pandas.DataFrame(school1)
print(sdf_2)

sdf_2 = pandas.DataFrame(school1)
sdf_2.to_csv('university.csv',index=False, encoding='cp949') # 파일이름, 인덱스 번호 유무, 유니코드(cp949: 엑셀파일 유니코드)


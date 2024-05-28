import pandas

df = pandas.read_csv('company.csv',encoding='cp949')

grouped_department = df.groupby('department')
# print(grouped_department.count())
print(grouped_department.value_counts()) # 그룹 별로 묶인 안의 내용물을 보여줌
print(grouped_department['age'].mean())
print(grouped_department['salary'].mean()) # mean(): 평균
print(grouped_department['salary'].std()) # std(): 표준편차
print(grouped_department['salary'].value_counts())

grouped_age = df.groupby('age')
print(grouped_age.count()) # 숫자들을 보여줌


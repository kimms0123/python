import pandas

df = pandas.read_csv("company.csv", encoding='cp949')
# 기본 열 뽑기
# print(df['name']) # 이름만 가져옴 (하나 열)
# print(df['age']) # 연봉
# print(df['salary']) # 나이
# print(df[['name', 'age', 'salary']]) # 다중 열

# 조건부 열 뽑기
# a = df['salary'] >= 5000
# b = df['years_at_company'] >= 7
# print(df[a & b])

# print(df[df['salary'] >= 7000])

# 근무 년 수 7년 이상
# print(df[df['years_at_company'] >=7])

# 우수사원: 근속연도 10, 만족도 8이상, 수행도 80점 이상
# years = df['years_at_company'] >= 10
# satisfaction = df['job_satisfaction'] >= 8
# performance = df['performance_score'] >= 80
# print(df[years & satisfaction & performance])

# 열 추가
# df['test'] = df['age'] * df['years_at_company']
# print(df)

# 근속일수에 따른 직급
# 5년 이하: 사원-10년 이하: 과장-15년 이하: 부장
def makeRank(x):
    if x <= 5:
        return "사원"
    elif x < 10:
        return "과장"
    else:
        return "부장"

# apply 함수
# df['rank'] = df['years_at_company'].apply(makeRank)
# print(df)

# 인사 평가
# 20 이하: 권고 사직-50 이하: 직급 유지-80 이하: 보너스-100: 승진
def makeRate(x):
    if x <=20:
        return "권고 사직"
    elif x <= 50:
        return "직급 유지"
    elif x <= 80:
        return "보너스"
    else:
        return "승진"
df['rate'] = df['performance_score'].apply(makeRate)
print(df)

print(df.info()) # 어떤식으로 생겼는지 알려줌
print(df.describe()) # 필드 안에 들어간 내용을 자세하게 알려줌

print(df.sort_values(by='name'))
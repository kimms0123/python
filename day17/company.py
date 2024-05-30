import pandas
from faker import Faker
import random
f = Faker('ko_KR')
age = [20,30,40,50,60]
salary = [3000 + x *500 for x in range(14)]
department = ["영업부","사업부","개발부","경영부","인사부","생산부"]

data = {
    'name': [f.name() for x in range(300)],
    'age': [random.choice(age) for x in range(300)],
    'salary': [random.choice(salary) for x in range(300)],
    'department': [random.choice(department) for x in range(300)],
    'years_at_company': [random.randint(1,15) for x in range(300)],
    'job_satisfaction': [random.randint(1,10) for x in range(300)],
    'performance_score': [random.randint(1,100) for x in range(300)]
}
df = pandas.DataFrame(data)
print(df)

df = pandas.DataFrame(data)
df.to_csv('company.csv',index=False, encoding='cp949')

# RentCar.DB
# car: 차 고유번호, 차 이름, 차 색상, 제조사
# member: 아이디, 이름, 주소, 전화번호
# Reserve: 예약 번호, 예약 차 번호, 예약 시작 일자
# 1.  자동차 등록 -> 차 고유번호, 차이름, 차 색상, 차 제조사를 입력받고 cartable에 넣기
# 2. 멤버 등록 -> 아이디, 이름, 주소, 전화번호 입력받고 Menber Table에 넣기

import sqlite3
connection = sqlite3.connect('RentCar.db')
cursor = connection.cursor()

sql = """
CREATE TABLE CAR (
    car_id INTEGER PRIMARY KEY,
    name VARCHAR(10),
    color VARCHAR(20),
    company VARCAHR(20)
)
CREATE TABLE MEMBER(
    userID INTEGER(30) PRIMARY KEY,
    userName VARCHAR(10),
    userAdd VARCHAR(20),
    phonenum VARCHAR(40)
)
CREATE TABLE RESERVE(
    bookNum INTEGER PRIMARY KEY,
    CarNum INTEGER,
    startDate DATE
)
""" # 따로 넣어야함

cursor.execute(sql)
connection.commit()
cursor.close()
# db 연결
import sqlite3

connection = sqlite3.connect('RentCar.db')
cursor = connection.cursor()

# 자동차 등록
print("렌트카 프로그램")
while (True):
    codeNum = input("1. 자동차 등록 2. 멤버 등록 3. 예약하기(업데이트 중) 4. 프로그램 종료>>")

    # 자동차 등록
    if codeNum == "1":
        carNumber = input("차 고유 번호 입력")
        carName = input("차 이름 입력")
        color = input("차 색상 입력")
        company = input("차 제조사 입력")
        sql = f"""
        INSERT INTO CAR(car_id, name, color, company)
        VALUES('{carNumber}', '{carName}', '{color}', '{company}')
        """
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        print("데이터베이스 저장 완료!")

    # 멤버 등록
    if codeNum == "2":
        id = int(input("아이디 입력: "))
        name = input("이름 입력: ")
        add = input("주소 입력: ")
        phone = input("전화번호 입력: ")
        sql = F"""
        INSERT INTO MEMBER(userID, userName, userAdd, phonenum,)
        VALUES('{id}', '{name}', '{add}', '{phone}')
        """
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        print("유저 정보 저장 완료!")

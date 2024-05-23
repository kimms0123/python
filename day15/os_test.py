import os
import datetime
import random
from review import yearToZodiac

# print(os.getlogin())

# 바탕화면 경로 따기
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# 바탕화면 경로와 폴더 이름 합치기
folder_path = os.path.join(desktop_path, '과장님부당업무지시폴더')
# 폴더 만들기
os.mkdir(folder_path)

# 오늘 날짜 가져오기
start_today = datetime.date.today()

for x in range(365):
    date_folder = start_today + datetime.timedelta(days=x)
    path = os.path.join(folder_path, date_folder.strftime("%Y-%m-%d"))
    os.mkdir(path)



# 폴더: 용띠의해_5월_23일_목요일

# 바탕화면 경로 따기
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# 바탕화면 경로와 폴더 이름 합치기
folder_path = os.path.join(desktop_path, '과장님_부당업무지시폴더')
# 폴더 만들기
os.mkdir(folder_path)

# 오늘 날짜 가져오기
start_today = datetime.date.today()

for x in range(365):
    date_folder = start_today + datetime.timedelta(days=x)
    year_Zodiac = yearToZodiac(int(date_folder.strftime("%Y")))
    folder_name = f"{year_Zodiac}띠의해_{date_folder.strftime('%m_%d_%A')}"
    path = os.path.join(folder_path, folder_name)
    os.mkdir(path)


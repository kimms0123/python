# set (집합)
# 중복 허용 안 되는 타입
a = {1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8}
burgerking = {"새우 와퍼", "불고기 와퍼", "치즈 와퍼", "스테이크 와퍼"}
monstouch = {"새우 와퍼", "치즈 와퍼", "싸이 버거", "불고기 버거"}

x = burgerking.intersection(monstouch)
print(x)
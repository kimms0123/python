# enumerate: 열거하다
coffee = [{'name': '아메리카노', 'price': 2000}, {'name': '라떼', 'price': 3000}]

for index, item in enumerate(coffee):
    print(f"{index}. {item['name']} {item['price']}원")
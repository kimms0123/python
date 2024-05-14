from coffee.coffee import Coffee
from Inventory.inventory import Inventory

itKoreaInventory = Inventory()
itKoreaInventory.add_coffee(Coffee("아메리카노",3000))
itKoreaInventory.add_coffee(Coffee("에스프레소",2500))
itKoreaInventory.add_coffee(Coffee("복숭아 아이스티",4500))

print(itKoreaInventory.get_inventory())
# {'아메리카노': <coffee.coffee.Coffee object at 0x0000020C665F7710>,···
#               ↑ 메모리의 주소 값을 가르킴

# a는 {'아메리카노':Coffee("아메리카노":3000)}
a = itKoreaInventory.get_inventory()
print(a['아메리카노'])
print(a['아메리카노'].get_name())
print(a['아메리카노'].get_price())
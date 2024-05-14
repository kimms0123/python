from cafe.Inventory.inventory import Inventory
from cafe.coffee.coffee import Coffee

class Application:
    def __init__(self):
        self.inventroy = Inventory()

    def run(self):
        while True:
            print("1. 커피 판매")
            print("2. 커피 추가")
            print("3. 프로그램 종료")
            action = int(input("원하는 작업 번호 입력:"))

            if action == 1:
                self.handle_sale()
            elif action == 2:
                self.handle_add_menu()

            elif action == 3:
                print("프로그램 종료")
                break
            else:
                print("잘못 입력하셨습니다. 다시 시도해주세요.")

    def handle_add_menu(self):
        coffee_name = input("커피 이름:")
        coffee_price = int(input("커피 가격:"))
        self.inventroy.add_coffee(Coffee(coffee_name,coffee_price))
        print(f"{coffee_name}가 메뉴에 추가 되었습니다")

    def handle_sale(self):
        inventory_items = self.inventroy.get_inventory()
        # 인벤토리가 비어있을 경우
        if not inventory_items:
            print("판매할 커피가 없습니다. 먼저 커피를 추가하세요.")
            return
        # 인벤토리에 메뉴가 있을 경우
        print("판매할 커피를 선택하세요")
        for index, (name, coffee) in enumerate(inventory_items.items()):
            print(f"{index}. {coffee.get_name()} {coffee.get_price()}원")

        choice = int(input("번호를 입력하세요:"))
        coffeeList = list(inventory_items.keys())
        selectedCoffee = inventory_items[coffeeList[choice]]
        print(f"{selectedCoffee.get_name()}가 판매 되었습니다. 가격은 {selectedCoffee.get_price()}입니다.")
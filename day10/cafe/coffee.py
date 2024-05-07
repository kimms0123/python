class Coffee:
    def __init__(self, a, b):
        self.name = a
        self.price = b

    def intro(self):
        return f"{self.name} {self.price}원"

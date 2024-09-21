class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

# 상품 생성
product1 = Product("Apple", 1.5)
product2 = Product("Banana", 0.8)

# 주문 생성
order = Order()
order.add_item(product1, 2)
order.add_item(product2, 3)

# 총액 계산
total_price = order.calculate_total()
print("총 주문 금액:", total_price)
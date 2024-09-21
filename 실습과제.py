import decimal

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = decimal.Decimal(price)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

class Order:
    def __init__(self):
        self.products = []
        self.total = decimal.Decimal(0)

    def add_item(self, product):
        self.products.append(product)
        self.total += product.get_price()

    def get_item(self, name):
        for product in self.products:
            if product.get_name() == name:
                return product
        return None

    def remove_item(self, name):
        for i, product in enumerate(self.products):
            if product.get_name() == name:
                del self.products[i]
                self.total -= product.get_price()
                return True
        return False

    def calculate_final_price(self, tax_rate):
        return self.total * (1 + tax_rate).quantize(decimal.Decimal('0.01'))

# 테스트 코드
if __name__ == "__main__":
    order = Order()
    product1 = Product("Apple", "1.50")
    product2 = Product("Banana", "0.75")

    order.add_item(product1)
    order.add_item(product2)

    print(order.get_item("Apple").get_price())
    order.remove_item("Banana")
    print(order.calculate_final_price(decimal.Decimal("0.1")))
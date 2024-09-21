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

def main():
    order = Order()
    while True:
        print("1. 제품 추가")
        print("2. 제품 조회")
        print("3. 제품 삭제")
        print("4. 주문 내역 조회")
        print("5. 최종 가격 계산 (세금 포함)")
        print("6. 프로그램 종료")

        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            name = input("제품 이름: ")
            price = input("제품 가격: ")
            product = Product(name, price)
            order.add_item(product)
        elif choice == "2":
            name = input("조회할 제품 이름: ")
            product = order.get_item(name)
            if product:
                print(f"제품 이름: {product.get_name()}")
                print(f"제품 가격: {product.get_price()}")
            else:
                print("해당 제품이 없습니다.")
        elif choice == "3":
            name = input("삭제할 제품 이름: ")
            if order.remove_item(name):
                print("제품 삭제 완료")
            else:
                print("해당 제품이 없습니다.")
        elif choice == "4":
            if order.products:
                print("주문 내역:")
                for product in order.products:
                    print(f"- {product.get_name()}: {product.get_price()}")
            else:
                print("주문 내역이 없습니다.")
        elif choice == "5":
            tax_rate = decimal.Decimal(input("세율 (예: 0.1): "))
            final_price = order.calculate_final_price(tax_rate)
            print(f"최종 가격 (세금 포함): {final_price}")
        elif choice == "6":
            break
        else:
            print("잘못된 메뉴 번호입니다.")

if __name__ == "__main__":
    main()
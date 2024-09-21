# 추상화 란 ? 실체 화가 되지 않는 부모 로부터 상속 받는 것
# 부모 클래스 내에 이름만 선언 되고 구현 부가 없는 추상 메서드 를 포함
# 상속 받은 클래스 는 반드시 추상 메서드 에 대해서 구현 해줘야 함
from abc import * # 추상 클래스 를 사용 하기 위해 import

class NetworkAdapter(metaclass=ABCMeta) : # 해당 클래스 를 추상 클래스 로 만듦
    @abstractmethod
    def connect(self):
        pass
class WiFi(NetworkAdapter):
    def __init__(self, company):
        self.company = company
    def connect(self):
        print(f"{self.company}의 와이 파이에 연결 되었 습니다. ")

class FiveG(NetworkAdapter):
    def __init__(self, company):
        self.company = company

    def connect(self):
        print(f"{self.company}의 5G에 연결 되었 습니다. ")

class Lte(NetworkAdapter) :
    def __init__(self, company):
        self.company = company

    def connect(self):
        print(f"{self.company}의 Lte에 연결 되었 습니다. ")

net = input("연결할 네트 워크 [1]wifi [2]5G [3]Lte : ")

if net == "1":
    adapter = WiFi("KT Mega pass")
elif net == "2":
    adapter = FiveG("SK Telecom")
elif net == "3" :
    adapter = Lte("LG U+")
else :
    print("연결할 네트 워크가 없 습니다")

adapter.connect()
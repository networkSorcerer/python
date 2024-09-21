# 다형성 이란 부모가 물려 준 특성을 재정의 사용 하는 것을 의미
# 오버 로딩 : 파이썬 에서 지원 하지 않음 ( 메서드 이름은 동일 하고 매개 변수의 갯수나 타입 으로 구분)
# 오버 라이딩 : 부모가 물려준 특성을 재정의 하는 것

def over_sum(x, y, z) :
    return x + y + z
print(over_sum(x=1, y=2, z=3)) # 정수에 대한 덧셉
print(over_sum(x=1.1, y=2.2, z=3.3)) # 실수에 대한 덧셈
print(over_sum("혜인","하니","민지")) # 문자열 덧셈


class PrototypeTv:
    def __init__(self, is_on, channel, volume):
        self.is_on = is_on
        self.channel = channel
        self.volume = volume
    def set_on(self, is_on):
        self.is_on = is_on
    def set_channel(self, chl):
        if 1 <= chl <= 1000:
            self.channel = chl
            print(f"채널은 {self.channel}로 변경하였습니다.")
        else :
            print(f"채널 설정 범위가 아닙니다.")

class ProductTv(PrototypeTv):
    def set_channel(self, chl):
        if 1 <= chl <= 2000:
            self.channel = chl
            print(f"채널은 {self.channel}로 변경하였습니다.")
        else:
            print(f"채널 설정 범위가 아닙니다.")

lg_tv = ProductTv(False, 20, 20 )
lg_tv.set_channel(1500)
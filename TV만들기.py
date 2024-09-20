# 클래스 란? 객체를 만들기 위한 설계 도면, 상태 값을 저장 하는 변수, 동작을 규정 하는 메서드 가 포함
# 키워드 는 class
# 객체란? 클래스 를 실체화 하는 것
# 상속 : 부모 클래스 의 특성을 ㅈ식 클래스 에 물려 주는 것
# 캡슐화 : 내부의 멤버(변수)을 외부 에서 접근할 수 없도록 하는것, 접근을 위한 게터와 세터 메서드 필요
# 다형성 : 부모의 특성을 물려 받아 특성을 변경 하거나 개선 하는 행위 (오버 로딩(x), 오버 라이딩(o))
# 추상화 : 객체화 가 되지 않는 부모로 부터 특성을 물려 받는 것 (추상 클래스)
# 클래스 이름 파스칼 표기법 (첫자가 대문자)
# 클래스 만들기 위해서 는 생성자 가 필요 (__init__())
# 생성자 는 클래스 가 객체로 만들어 질 때 불려 짐 (내부의 인스 턴스 변수를 초기화 하는 목적 으로 사용)
class Television :
    def __init__(self, name , is_on, channel, volume):
        self.name = name # 인스 턴스 변수를 생성 하고 생성자 의 매개 변수를 통해서 초기 값을 입력 받음
        self.is_on = is_on # TV의 전원 on/off
        self.channel = channel
        self.volume = volume
    def set_on(self, is_on): # 전원을 on/off 하는 세터 메서드
        self.is_on = is_on
    def set_channel(self, cnl):
        self.channel = cnl
    
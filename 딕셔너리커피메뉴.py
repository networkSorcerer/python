# 커피 메뉴 만들기
# [1] 메뉴 보기 [2] 메뉴 조회 [3] 메뉴 추가 [4] 메뉴 삭제 [5] 종료
# 기본 메뉴 만들기
from unicodedata import category

menu = {
    "Americano" : ["Coffee", 2000, "기본 커피 입니다."],
    "Espresso" : ["Coffee", 2500 , "진한 커피 입니다"],
    "Latte": ["Coffee", 4000, "우유가 들어 있는 커피 입니다."],
    "ColdBrew": ["Coffee", 4500, "연유가 들어 있는 커피 입니다."],
    "GreenTea": ["Tea", 4500, "녹차 입니다."],
    "BlackTea": ["Tea", 4500, "홍차 입니다."],
    "MilkTea": ["Tea", 4000, "우유가 포함된 차 입니다."],
    "PeachAde": ["Ade", 5000, "복숭아 에이드 입니다."],
    "GreenAde": ["Ade", 5000, "포도 에이드 입니다."],
    "LemonAde": ["Ade", 4500, "레몬 에이드 입니다."]
}

# [1]메뉴 보기
def print_menu() :
    # for key in menu :
    #     print(f"{key} : {menu[key]}")
    for key, value in menu.items():
        print(f"{key} : {value}")

print_menu()

# [2]메뉴 조회(개별 메뉴)
def get_menu(key) :
    if key in menu :
        print(menu[key])
    else :
        print("찾는 메뉴가 없 습니다.")

#[3] 메뉴 추가
def add_menu(key, category, price , desc) : # key, 분류, 가격, 설명
    if key not in menu : # 해당 키에 대한 메뉴가 없음
        menu[key] = [category, price, desc]
        print(f"{key} 메뉴가 추가 되었 습니다. ")
    else :
        print("메뉴가 이미 존재 합니다.")

# [4] 메뉴 삭제
def del_menu(key):
    if key in menu:
        del menu[key]
        print(f"{key}메뉴가 삭제 되었 습니다.")
    else :
        print("삭제 할 메뉴가 없습니다.")

while True :
    print("메뉴를 선택 하세요 : ")
    sel = input("[1]메뉴 보기 [2]메뉴 조회 [3]메뉴 추가 [4]메뉴 삭제 [5]종료 하기 : ")
    if sel == "1" :
        print_menu()
    elif sel == "2":
        key = input("조회할 메뉴 입력 : ")
        get_menu(key)
    elif sel == "3":
        key = input("추가할 메뉴 이름 : ")
        cate = input("분류 입력 : ")
        price = int(input("가격 입력 : "))
        desc = input("제품 설명 : ")
        add_menu(key, cate, price, desc)
    elif sel == "4" :
        key = input("삭제할 메뉴 입력 : " )
        del_menu(key)
    elif sel == "5":
        print("영업을 종료 합니다.")
        break
    else :
        print("잘 못된 입력 입니다.")

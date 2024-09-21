import json

def load_menu():
    try:
        with open("menu.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("메뉴 파일이 없습니다. 처음부터 시작합니다.")
        return {}
    except json.JSONDecodeError:
        print("메뉴 파일이 손상되었습니다.")
        return {}

def save_menu(menu):
    with open("menu.json", "w", encoding="utf-8") as f:
        json.dump(menu, f, ensure_ascii=False, indent=4)

def print_menu(menu):
    if not menu:
        print("메뉴가 없습니다.")
        return
    print("------------------ 메뉴 목록 ------------------")
    for idx, (key, value) in enumerate(menu.items(), start=1):
        print(f"{idx}. {key} ({value[0]}) - {value[1]}원: {value[2]}")

def get_menu_by_name(menu, name):
    if name in menu:
        print(f"{name}: {menu[name]}")
    else:
        print("해당 메뉴를 찾을 수 없습니다.")

def add_menu(menu):
    name = input("추가할 메뉴 이름: ")
    category = input("카테고리: ")
    price = int(input("가격: "))
    desc = input("설명: ")
    menu[name] = [category, price, desc]
    print(f"{name} 메뉴가 추가되었습니다.")

def delete_menu(menu):
    name = input("삭제할 메뉴 이름: ")
    if name in menu:
        del menu[name]
        print(f"{name} 메뉴가 삭제되었습니다.")
    else:
        print("해당 메뉴를 찾을 수 없습니다.")

def modify_menu(menu):
    name = input("수정할 메뉴 이름: ")
    if name in menu:
        print(f"현재 {name} 메뉴 정보: {menu[name]}")
        category = input("새로운 카테고리 (빈칸으로 생략): ") or menu[name][0]
        price = int(input("새로운 가격 (빈칸으로 생략): ")) or menu[name][1]
        desc = input("새로운 설명 (빈칸으로 생략): ") or menu[name][2]
        menu[name] = [category, price, desc]
        print(f"{name} 메뉴가 수정되었습니다.")
    else:
        print("해당 메뉴를 찾을 수 없습니다.")

def search_menu(menu):
    keyword = input("검색어: ")
    results = [item for item in menu.items() if keyword in item[0] or keyword in item[1][2]]
    if results:
        print("검색 결과:")
        for idx, (key, value) in enumerate(results, start=1):
            print(f"{idx}. {key} ({value[0]}) - {value[1]}원: {value[2]}")
    else:
        print("검색 결과가 없습니다.")

def sort_menu(menu):
    sort_by = input("정렬 기준 (name, price, category): ")
    reverse = input("역순 정렬 (yes/no): ").lower() == "yes"
    if sort_by == "name":
        sorted_menu = dict(sorted(menu.items(), key=lambda x: x[0], reverse=reverse))
    elif sort_by == "price":
        sorted_menu = dict(sorted(menu.items(), key=lambda x: x[1][1], reverse=reverse))
    elif sort_by == "category":
        sorted_menu = dict(sorted(menu.items(), key=lambda x: x[1][0], reverse=reverse))
    else:
        print("잘못된 정렬 기준입니다.")
        return
    print_menu(sorted_menu)

# 메뉴 로드
menu = load_menu()

while True:
    print("------------------ 메뉴 관리 시스템 ------------------")
    print("1. 메뉴 보기")
    print("2. 메뉴 조회")
    print("3. 메뉴 추가")
    print("4. 메뉴 삭제")
    print("5. 메뉴 수정")
    print("6. 메뉴 검색")
    print("7. 메뉴 정렬")
    print("8. 메뉴 저장")
    print("9. 종료")
    choice = input("메뉴 선택: ")

    if choice == "1":
        print_menu(menu)
    elif choice == "2":
        name = input("조회할 메뉴 이름: ")
        get_menu_by_name(menu, name)
    elif choice == "3":
        add_menu(menu)
    elif choice == "4":
        delete_menu(menu)
    elif choice == "5":
        modify_menu(menu)
    elif choice == "6":
        search_menu(menu)
    elif choice == "7":
        sort_menu(menu)
    elif choice == "8":
        save_menu(menu)
    elif choice == "9":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 메뉴를 선택하셨습니다.")
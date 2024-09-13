# 햄버거 가격 3개
# 음료 가격 2개
# 출력 : 세트 메뉴 가격 = 햄버거 3개 중 제일 싼거 + 음료 2개 중 싼거 - 50
# 입력 : 1000 1500 3000 1200 750
# 세트 : 1700원

# berger = [1000, 1500 , 3000] # number[:3]
# drink = [1200, 750] # number[3:]
# chipBerger = min(berger)
# chipDrink = min(drink)
# set = chipBerger + chipDrink - 50
# print(set)

ls = list(map(int, input("입력 : ").split()))
# min_b = min(ls[:3])
# min_d = min(ls[3:])
# print(f"{min_b + min_d - 50}")
min_berger = ls[0]
min_drink = ls[3]

for i in range(len(ls)) :
    if i < 3 and min_berger > ls[i] :
        min_berger = ls[i]
    if i > 2 and min_drink > ls[i] :
        min_drink = ls[i]

print(f"세트 가격 : {min_berger + min_drink - 50}")
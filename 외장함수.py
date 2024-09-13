# 외장 함수는 import 해서 사용 하는 함수, 파이썬 기본 적으로 제공 하는 것
# 랜텀 함수 : 지정한 범위내에서 임의의 숫자를 만들어 내는 것
import random

for i in range(30):
    rand = random.randint(1, 11)  # 0 ~ 10 까지의 임의의 값을 생성 randrange는 10미만의 수
    print(rand, end=" ")
print()

# 중복 되지 않는 로또 번호 생성 : 1 ~ 45 사이의 임의의 수 6개
# 리스를 사용 하고, 리스트 내에 임의로 생성한 번호가 있으면 , 추가 하면 안됨
# if rand not in list
# print("로또 번호 자동 생성 : ")
# lotto = []
# while True:
#     rand = random.randrange(1,46)
#     if rand not in lotto:
#         lotto.append(rand)
#     if len(lotto) == 6: break
# print(lotto)
# # 빈 리스트 생성
# lotto_numbers = []
#
# # 6개의 중복되지 않는 로또 번호 생성
# while len(lotto_numbers) < 6:
#     rand = random.randint(1, 45)  # 1부터 45 사이의 임의의 숫자 생성
#     if rand not in lotto_numbers:  # 리스트에 없는 경우에만 추가
#         lotto_numbers.append(rand)
#
# # 생성된 로또 번호 출력
# print(lotto_numbers)
# lotto = set() # 집합은 자동 적으로 중복이 제거 된다
# while len(lotto) < 6:
#     rand = random.randrange(1, 46)
#     lotto.add(rand)
# print(lotto)

lotto =[]

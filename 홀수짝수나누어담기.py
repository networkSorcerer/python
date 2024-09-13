import random

# 집합은 중복을 허용하지 않음
lotto = set()  
even = set()  # 짝수를 담을 집합
odd = set()     # 홀수를 담을 집합

# 1부터 45까지의 숫자 중에서 중복되지 않는 6개의 숫자를 lotto에 추가
while len(lotto) < 6:
    rand = random.randrange(1, 46)
    lotto.add(rand)

# 생성된 로또 번호를 홀수와 짝수로 나누어 double과 odd에 추가
for number in lotto:
    if number % 2 == 0:
        even.add(number)
    else:
        odd.add(number)

print("짝수 집합:", even)
print("홀수 집합:", odd)


number = list(map(int, input("입력 : ").split()))
odd = list(filter(lambda x : x % 2 == 1, number))
even = list(filter(lambda x : x % 2 == 0, number))
print(f"홀수 : {odd}")
print(f"짝수 : {even}")
# even = []
# odd = []
#
# for e in number :
#     if e % 2 == 0 : even.append(e)
#     else : odd.append(e)
# print(f"홀수 : {odd}")
# print(f"짝수 : {even}")
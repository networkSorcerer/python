# 영식(Y) 요금제 : 30초마다 10원
# 민식(M) 요금제 : 60초마다 15원
# 3 <= 통화 횟수
# 40 40 40 <= 각 통화당 통화 시간
# M 45 <= 더 싼 요금제와 통화 요금
# Y M 50 <= 두개의 요금의 통화 총 금액이 같은 경우

# 통화 횟수 입력

# 각 통화에 대한 통화 시간 입력

# 통화 시간에 대한 리스트를 순회하면서 총 통화 시간 누적
# 민식과 영식 요금제에 대한 총 통화 요금을 누적하고 둘 중 싼걸 찾아야 함
# 만약 같은 Y M으로 출력
import random
total =0
call =[]
while True :
    phonePay = int(input("출력할 통화 수 : 3미만 : "))
    if  phonePay > 3  :
        print("3미만 입력")
        continue
    for i in range(phonePay):
        rand = random.randint(1, 10000)  # 0 ~ 10 까지의 임의의 값을 생성 randrange는 10미만의 수
        print(rand, end=" ")
        call.append(rand)
    print()
    for j in range(0,phonePay,+1) :
        total += call[j]
        young = int(total/ 30 * 10 + 10)
        minsic = int(total/ 60 * 15 + 15)
    print(f"영식 요금제 적용시 : {young}")
    print(f"민식 요금제 적용시 : {minsic}")
    result = min(young, minsic)
    print(f"최소 요금 : {result}")

# n = int(input())
# call = list(map(int, input().split()))
#
# y_pay = m_pay = 0
# for i in range(n):
#     y_pay += (call[i] // 30) * 10 + 10
#     m_pay += (call[i] // 60) * 15 + 15
#
# if y_pay > m_pay:
#     print("M", m_pay)
# elif y_pay < m_pay:
#     print("Y", y_pay)
# else:
#     print("Y M", y_pay)
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

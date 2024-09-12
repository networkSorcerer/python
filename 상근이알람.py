# 상근이 알람 : 45분 일찍 알람을 울리 도록 하는 문제
# 입력 : 시간과 분을 입력 받음, 24시간제
# 22:40 => 21:55
# 00:30 => 23:45

# 입력은 h, m으로 : 기준 으로 입력
h, m = map(int, input("시간 입력 : ").split(":"))
# 시간을 분으로 환산 하기
calc_min = h * 60 + m # 입력 받은 시간을 모두 분으로 환산
# 분으로 환산 하는 시간이 45보다 작으면 시간을 별도 계산 해야 함
if calc_min < 45 :
    calc_min = 24 * 60 + m
# 45분을 빼줌
calc_min -= 45

# 다시 시간과 분으로 환산 해서 출력
print(f"{calc_min // 60}:{calc_min % 60}")
# 참고
# 24 시간 제로 시간을 : 기준 으로 입력을 받아서 시, 분, 초로 찍는데 12 시간 제로 변환ㄴ
# hour, min, sec = map(int, input("시:분:초 :").split(":"))
#
# if hour > 12 :
#     hour -= 12 # hour = hour = -12
#     print(f"오후 {hour}시 {min}분 {sec}초")
# else :
#     print(f"오전 {hour} 시 {min} 분 {sec}초")

# h , m = map(int, input("시:분").split(":"))
# if m < 45 :
#     last = 45- m
#     m = 60 - last
#     h -= 1
#     print(f"{h}시 : {m}분")
# else :
#     m -= 45
#     print(f"{h}시 : {m}분")



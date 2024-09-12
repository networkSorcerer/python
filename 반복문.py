# 조건이 참인 동안 반복 수행

n = int(input("정수 입력 :"))
sum = 0 # 값을 누적 하기 위한 변수
while n : # 0이 아닌 모든 값은 참으로 간주 (자바 제외)
    sum += n
    n -= 1 # n = n -1 , n--
print(sum)
for i in range(1, n+1): # 범위 기반의 for 문
    sum += i
print(sum)

# while 반복 횟수가 정해 지지 않은 조건문 , for 은 정해져 있음
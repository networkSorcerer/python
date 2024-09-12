# 조건이 참인 동안 반복 수행
#
# n = int(input("정수 입력 :"))
# sum = 0 # 값을 누적 하기 위한 변수
# while n : # 0이 아닌 모든 값은 참으로 간주 (자바 제외)
#     sum += n
#     n -= 1 # n = n -1 , n--
# print(sum)
# for i in range(1, n+1): # 범위 기반의 for 문
#     sum += i
# print(sum)
#
# # while 반복 횟수가 정해 지지 않은 조건문 , for 은 정해져 있음
# while True : # 반복문 내에 탈출 조건이 있어야 함
#     age = int(input("나이를 입력 하세요 : "))
#     if 0 <= age <= 200 : break # 정상 적인 입력 이므로 반복문 탈출
#     print("나이를 잘 못 입력 하셨 습니다.")
# print(f"당신의 나이는 {age} 입니다.")
#
# while True :
#     score = int(input("성적 입력 : "))
#     if 0 <= score <= 100 : break
#     print("0~ 100의 값을 입력해주세요")
#
# while True:
#     score = int(input("성적 입력 : "))
#     if 0 <= score <= 100:
#         if score >= 90:
#             print("A")
#         elif score >= 80:
#             print("B")
#         elif score >= 70:
#             print("C")
#         elif score >= 60:
#             print("D")
#         else:
#             print("F")
#         break
#     else:
#         print("0에서 100 사이의 숫자를 입력 하세요.")
#
# # for 문 : 정해진 범위 만큼을 반복 수행 할 때 효과적
# # for 요소 in 시퀀스 : 시퀀스 자료에 대한 자동 순회,
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits :
#     print(fruit)
#
# name  = "asdkfljalsd"
# for e in name :
#     print(e, end="-")
# print()
# for e in input("문자열 입력 : ") :
#     print(e, end="-")
# # for 인덱스 in range(시작값, 종료값, 증감값):
# n = int(input("정수값 입력 : "))
# sum = 0
# for i in range(n +1) : # 시작 값이 0인 경우 생략 가능 , 증감 값이 1인 경우 생략 가능
#     sum += i
# print(sum)

# # 이중 for 문 사용하기
# n = int(input("정수 입력 : "))
# for i in range(n): # 0 ~ n 미만 까지
#     print(f"i={i} ", end="")
#     for j in range(n) :
#         print("*", end=" ")
#     print()

# 이중 for 문 구구단 찍기
# for i in range(2,10) : # 2단에서 9단
#     for j in range(1,10):
#         print(f"{i} X {j} = {i * j}")
#     print("-"*20)

# 제어문 : break, continue
# break : 반복 문을 탈출 할 때 사용
# continue : 아래의 문장을 수행 하지 않고 반복 문의 조건 식으로 이동 ,(해당 루틴은 수행된 걸로 간주)

# n = int(input("정수 입력 : "))
# for i in range(n) :
#     if i % 2 == 0 : continue # 짝수 이면 아래의 문장을 수행 하지 않음
#     print(i)

# 반복 문을 반대로 수행 하기
n = int(input("정수 입력 : "))
for i in range(n, 0-1, -1) : # 시작값 , 최종값, 증감값
    print(f"인덱스 : {i}")

# for 문으로 알파벳 출력 하기
# ASCII 0
# chr() : 유니 코드를 입력 받아 그 코드에 해당 하는 문자를 출력
# ord() : 문자의 유니 코드 값을 돌려 주는 함수

for i in range(ord("A") , ord("z")+1) :
    print(chr(i), end=" ")

for i in range(65, 91) :
    print(chr(i), end=" ")
print()
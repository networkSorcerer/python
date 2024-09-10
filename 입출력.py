# 표준 입출력 : 콘솔 입출을 의미"
# [] 대괄호 : 리스트를 표시
# {} 중괄호 : 딕셔너리 표시
# () 소괄호 : 함수의 인수, 튜플 사용
# print() : 화면 출력을 위한 함수
from time import sleep

# print(36)
# print("문자열")
# print([1,2,3]) #리스트 출력
# print("파" + "이" + "썬") # + 문자열을 이어주는 연산자
# print("파","이","썬", sep="") # , (콤마) 구분자를 의미, 구분자의 기본값을 의미
# print("파""이""썬")
# 이스케이프 문자 : 출력 구간의 흐름을 제어
# \n(줄바꿈), \t (탭을 의미), \b(백스페이스)를 의미. \r(커서를 맨 앞으로 돌림)
# print("", sep =" ",  end="\n")
# print("Banana\b")
# print("Banana\rApple") #
# print("Banana","Apple","Mango",sep="$")
# year = 2024
# month = 9
# day = 10
# print(year, month, day, sep="-")

import time

# for i in range(1, 101):
#     time.sleep(1)
#     print(f"\r{i}%", end="")

# 출력 스타일 정리
name = "정경수"
age = 22
gender = "남성"
job = "개발자"
addr = "경기도 수원시"

# 서식 지정자 스타일 (C언어 방법)
print("========== 서식 지정자 스타일 ============")
print("이름 : %s, 성별 : %s "%(name, gender))
print("나이 : %d"%age)
print("주소 : %s"%addr)

# 파이썬 old 스타일
print("========== 파이썬 OLD 스타일 ============")
print("이름 : {}  성별 : {} ".format(name, gender))
print("주소 : {}".format(addr))

# 파이썬의 현재 스타일
print(f"이름 : {name} 성별 : {gender}")
print(f"주소 : {addr}")

# 문자열 연결 연산자 사용 방식
print("이름 :" + name)
print("나이 : " + str(age)) # 그냥 정수를 바로 넣으면 에러뜸

# 정렬
num1 = 10
num2 = 100
num3 = 1000
num4 = 10000
num5 = 3.1459294584

print(f"|{num1:8}|") # :8는 공간을 8자리 지정함, 우측 정렬
print(f"|{num2:<8}|")  # 좌측 정렬
print(f"|{num3:^8}|") # 중간 정렬
print(f"|{num4:8}|")
print(f"{num5:.3f}") # 소수점 반올림
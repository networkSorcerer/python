from datetime import datetime
from idlelib.iomenu import encoding
from importlib.resources import contents

# 파일을 읽거나 쓰기 위해서는 우선 파일을 open해야 합니다
# 파일 객체 = open(파일명, 파일모드, 인코딩)
# open 이후 작업 완료 후 반드시 close 해야 합니다 (with 키워드를 사용하면 생략 가능합니다)
# encoding = "utf-8" 은 한글 깨짐 방지를 위한 인코딩

# r 읽기 모드 - 파일을 읽기 위해 사용
# w 쓰기 모드 - 파일에 내용을 쓸때 사용 (기존의 파일 지워짐)
# a 추가 모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용

# 파일을 열 때 경로는 절대 경로 상대 경로 로 지정할수 있습니다
# path를 지정하지 않으면 현재 터미널 위치에 생성 됩니다)

# score_file = open("score.txt","w", encoding="utf-8")
#score_file = open("score.txt","a", encoding="utf-8") # append
# print("수학 : 0", file=score_file)
# print("영어 : 0", file=score_file)
# score_file.write("과학 : 80" + "\n")
# score_file.write("코딩 : 100" + "\n")
# score_file.close()

# with 키워드
# 프로그램으 코드 길이가 길어지면 open() 과 close() 사이에 많은 코드가 들어가
# close 를 호출하지 않아 발생하는 문제를 해결할수 있습니다 즉 , with 구문을 사용하게 되면 ,
# 구문이 종료 될때 자동으로 파일이 닫힙니다

import os

from 내장함수 import my_list

# if os.path.exists('textfile.txt'):
#     with open('textfile.txt', 'r') as file:
#         contents = file.read()
# else:
#     print('파일이 존재하지 않습니다.')


# 위 구문과 동일한 내용
# file = open('textfile.txt', 'r')
# contents = file.read()
# file.close()
#
# from datetime import datetime
#
# with open("password.txt", "w") as f:
#     date = str(datetime.today().year) + str(datetime.today().month) \
#         + str(datetime.today().day)
#     while True:
#         url = input("사이트 : ")
#         if url == "exit": break
#         my_str = url.replace("http://", "")
#         my_str = my_str[:my_str.index(".")] # 슬라이싱, 처음부터 . 위치 미만까지
#         password = my_str[:3] + str(len(my_str)) + str(my_str.count("o")) + date + "!" + "jks"
#         print("비밀번호 : " + password)# 각 사이트 비밀번호 자동으로 만들기
#         f.write(password + "\n")

# pickle 파이썬 피클(Pickle)은 파이썬 객체를 직렬화(serialize)하고 역직렬화(deserialize)하기 위한 모듈입니다.
# 피클을 사용하면 파이썬 객체를 파일에 저장하거나 네트워크를 통해 전송할 수 있습니다.
# 피클은 객체를 이진 형식으로 변환하여 저장하며, 나중에 필요할 때 객체를 원래의 상태로 복원할 수 있습니다.

import pickle

# 객체를 직렬화하여 파일에 저장하기
# data = {'name': 'Alice', 'age': 30, 'city': 'New York'}
# with open('data.pickle', 'wb') as file:
#     pickle.dump(data, file)
# print()
# # 파일에서 객체를 역직렬화하여 복원하기
# with open('data.pickle', 'rb') as file:
#     restored_data = pickle.load(file)
#
# print(restored_data)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}

# 데이터 정의 (멀티라인 문자열)
# data = """
# 날짜     에스프레소  아메리카노  카페라떼  카푸치노
# 9.11 10 50 45 20
# 9.12 12 45 41 18
# 9.13 11 53 32 25
# 9.14 15 49 38 22
# """
#
# # 'coffee_sales.txt' 파일에 저장
# with open('coffee_sales.txt', 'w', encoding='utf-8') as file:
#     file.write(data)

# print("데이터가 'coffee_sales.txt'에 저장되었습니다.")
#
# file_name = "coffee_sales.txt"
#
# f = open(file_name, "r", encoding="utf-8")  # 파일 읽기
# header = f.readline()  # 데이터의 첫 번째 줄을 읽음
# header_line = header.split()  # 첫 줄의 문자열을 분리한 후 리스트로 변환

# for line in f:  # 두 번째 줄부터 데이터를 읽어서 반복 처리
#     data_list = line.split()  # 문자열으 분리해서 리스트로 변환
#     print(data_list)  # 결과 확인을 위해 리스트 출력
#
# f.close()  # 파일 닫기
#

# 데이터 정의 (멀티라인 문자열)
data = """
날짜     에스프레소  아메리카노  카페라떼  카푸치노
9.11 10 50 45 20
9.12 12 45 41 18
9.13 11 53 32 25
9.14 15 49 38 22
"""

# 'coffee_sales.txt' 파일에 저장
with open('coffee_sales.txt', 'w', encoding='utf-8') as file:
    file.write(data)

# 파일에서 데이터를 읽어서 분석
file_name = "coffee_sales.txt"

# 파일 읽기
with open(file_name, "r", encoding="utf-8") as f:
    header = f.readline().strip()  # 데이터의 첫 번째 줄을 읽음
    header_list = header.split()   # 첫 줄의 문자열을 분리한 후 리스트로 변환

    espresso = []
    americano = []
    cafelatte = []
    cappucino = []

    for line in f:  # 두 번째 줄부터 데이터를 읽어서 반복 처리
        data_list = line.split()  # 문자열을 분리해서 리스트로 변환
        # 커피 종류별로 정수로 변환한 후, 리스트의 항목으로 추가
        espresso.append(int(data_list[1]))
        americano.append(int(data_list[2]))
        cafelatte.append(int(data_list[3]))
        cappucino.append(int(data_list[4]))

# 결과 출력
print(f"{header_list[1]} 전체 판매량 : {sum(espresso)}, 일 평균 판매량 : {sum(espresso) / len(espresso):.2f}")
print(f"{header_list[2]} 전체 판매량 : {sum(americano)}, 일 평균 판매량 : {sum(americano) / len(americano):.2f}")
print(f"{header_list[3]} 전체 판매량 : {sum(cafelatte)}, 일 평균 판매량 : {sum(cafelatte) / len(cafelatte):.2f}")
print(f"{header_list[4]} 전체 판매량 : {sum(cappucino)}, 일 평균 판매량 : {sum(cappucino) / len(cappucino):.2f}")

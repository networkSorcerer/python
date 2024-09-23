# 모듈 이란? 파이썬 코드를 포함 하는 파일(.py)
# 패키지? 여러 모듈을 포함 하는 디렉 토리
#
# import math # math 모듈을 import
# print(math.sin(1))
# print(math.cos(1))
#
# from math import *
# print(sin(1))
# print(cos(1))

from datetime import datetime
#
# import math as m
# print(m.sin(1))
# print(m.cos(1))
#
# import sys
# # sys 모듈 : 시스템 과 관련된 정보를 가지고 있는 모듈
# print("명령줄 인수 : ",sys.argv)
#
# print("실행 경로 : ", sys.path[0])
#
# import os
#
# # 현재 작업 디렉토리
# cwd = os.getcwd()
# print("현재 작업 디렉토리:", cwd)
#
# # 디렉토리 생성
# os.mkdir("mydir")
#
# # 파일 또는 디렉토리 존재 여부 확인
# is_file = os.path.isfile("myfile.txt")
# is_dir = os.path.isdir("mydir")
# print("myfile.txt는 파일인가?", is_file)
# print("mydir은 디렉토리인가?", is_dir)
#
# # 시스템 명령 실행
# os.system("ls -l")

# 모듈 만들기
def add(a, b) :
    return a + b

def sub(a, b) :
    return a - b

if __name__=="__main__":
   print(add(1, 4))
   print(sub(4,2))
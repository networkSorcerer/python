# 참고 파일입출력
from idlelib.iomenu import encoding

#색깔을 출력하고 색깔을 3개 고르는데
# 예를 들어 violet green yellow 이면 750000 의 결과값이 나오도록 코딩
# 데이터 정의 (멀티라인 문자열)
# data = """
# 색 값 곱
# black 0 1
# brown 1 10
# red 2 100
# orange 3 1000
# yellow 4 10000
# green 5 100000
# blue 6 1000000
# violet 7 10000000
# grey 8 100000000
# white 9 1000000000
# """
#
# # 'registance.txt' 파일에 저장
# with open('registance.txt','w', encoding='utf-8') as file:
#     file.write(data)
# # 파일에서 데이터를 읽어서 분석
# file_name = "registance.txt"
#
# # 파일 일기
# with open(file_name , "r", encoding="utf-8") as f:
#     header = f.readline().strip()
#     header_list = header.split()
#
#     color = []
#     number = []
#     multi = []
#
#
#     for line in f :
#         data_list = line.split()
#         color.append(int(data_list[0]))
#         number.append(int(data_list[1]))
#         multi.append(int(data_list[2]))
#
# first = input("첫번째 색을 입력 하세요.")
# second = input("두번째 색을 입력 하세요.")
# third = input("세번째 색을 입력하세요.")
#
# print(first)
# print(second)
# print(third)



# 데이터 정의 (멀티라인 문자열)
# data = """
# 색 값 곱
# black 0 1
# brown 1 10
# red 2 100
# orange 3 1000
# yellow 4 10000
# green 5 100000
# blue 6 1000000
# violet 7 10000000
# grey 8 100000000
# white 9 1000000000
# """
#
# # 'resistance.txt' 파일에 저장
# with open('resistance.txt', 'w', encoding='utf-8') as file:
#     file.write(data)
#
# # 파일에서 데이터를 읽어서 색상, 값, 곱 정보를 저장
# color_to_value = {}
# color_to_multiplier = {}
#
# with open('resistance.txt', 'r', encoding='utf-8') as f:
#     f.readline()  # 첫 번째 줄 헤더를 건너뜁니다.
#     for line in f:
#         parts = line.split()
#         color = parts[0]            # 색상
#         value = int(parts[1])        # 값
#         multiplier = int(parts[2])   # 곱
#         color_to_value[color] = value
#         color_to_multiplier[color] = multiplier
#
# # 사용자로부터 색상을 입력받기
# first = input("첫 번째 색을 입력하세요: ").strip().lower()
# second = input("두 번째 색을 입력하세요: ").strip().lower()
# third = input("세 번째 색을 입력하세요: ").strip().lower()
#
# # 입력된 색상에 해당하는 값 계산
# if first in color_to_value and second in color_to_value and third in color_to_multiplier:
#     resistance_value = (color_to_value[first] * 10 + color_to_value[second]) * color_to_multiplier[third]
#     print(f"저항값은: {resistance_value} 옴입니다.")
# else:
#     print("잘못된 색상이 입력되었습니다.")

color = "black", "brown", "red", "orange", "yellow", \
    "green", "blue", "grey", "white" ,"violet"
f_name = color.index(input()) # 해당 문자 열의 인덱스 반환
s_name = color.index(input())
t_name = color.index(input())
print(int(str(f_name) + str(s_name)) * (10 ** t_name))
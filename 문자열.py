# 문자열 이란? 문자로 이루어 진 데이터 의 집합
# "", '', """ """, ''' '''
# 인덱싱 : 시퀀스(리스크, 튜플, 문자열, input()) 자료 형에서 특정 위치의 요소를 선택 하는 작업
# 인덱싱 은 0부터 시작
# 슬라이 싱 : 시퀀스 자료 형에서 일부 테이터 를 추출 하는 것
#
# jumin = input("주민 등록 번호 입력 : ") # 991120 - 1234567
#
# gender = jumin[7]
# if gender == "1" or gender == "3" :
#     print("남성 입니다.")
# else :
#     print("여성 입니다.")
#
# print("성별 : " + jumin[7])
#
# # 태어난 년도를 구하기 위해서 슬라이 싱
# year = jumin[:2] # 0 에서 부터 2미만 , 0에서 부터 시작 되는 경우는 생략 가능
# year = int(year)
# if gender == "1" or gender == "2" :
#     year += 1900
# else :
#     year += 2000
# print(f"태어난 년도 : {year}")
#
# # 생일 출력 : 0720 => 7월 20일
# month = jumin[2:4]
# day = jumin[4:6]
# month = int(month)
# day = int(day)
#
# print(f"생일 : {month}월 {day}일")
#
# # 생년월일
# print("생년월일 : " + jumin[:6]) # 991122-1234567
# print("뒤 7자리 : " + jumin[7:]) # 7에서 끝가지
# print("뒤 7자리 : " + jumin[-7:]) # -1은 맨 뒤자리
#
# #print(jumin[14]) # error string index out of range
#
# life = "Life is too short, You need Python"
# tmp = life[0]+life[1]+life[2]+life[3]
# print(tmp)

#life[0] = "l" # 이거는 안된다

# 대 소문자 바꾸기 : upper(), lower()
a = "Hello Python Program..."
print(a.upper())
print(a.lower())

# 대 문자는 소 문자로 소 문자는 대 문자로 ...

# 문자열 변경 : replace("기존 문자열","바꿀 문자열")

b = "Hello Python Python Program..."
n_b = b.replace("Python", "javaScript")
print(n_b)

# 문자 열에 포함된 문자 갯수 세기 및 문자열 길이 구하기
# count() : 문자열 내장 메서드 로 문자 열에 포함된 문자의 갯수를 반환
# __len__() : 문자열 길이를 반환
# len() : 문자열 길이를 반환
c = "Hello Python Python Program..."
print(c.count("l")) # 해당 문자열에서 매개변수로 전달한 문자/문자열 반환
print(len(c)) # 문자열 길이 반환
print(c.__len__()) #

# 문자열 찾기 : find() rfind(), index()
# find() : 찾은 문자열의 시작 인덱스반환,  찾지 못하면 -1
# index() : 찾은 문자열의 시작 인덱스반환, 찾지 못하면 ValueError 발행하고 종료됨
# rfind() : 뒤에서 부터 문자열을 찾음, 찾은 문자열의 인덱스는 앞에서부터 계산
phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점찾기 , 가장 좋은 선물은 용서"
print(phrase.find("가장"))
print(phrase.rfind("가장"))
print(phrase.index("포기"))

print(phrase.find("나에게"))
# print(phrase.index("나에게"))

new_phrase = phrase.replace("가장","나에게")
print(new_phrase)

# 문자열 연산자 : + , *
def sum_ex(x, y) :
    return x + y
print(sum_ex(100, 200))
print(sum_ex(3.14, 5.88))
print(sum_ex("korea","seoul"))

# 문자열 연산자 : + , *
print("태양고" + "나희도")
print("!"*10)
list = [0]*10
print(list)

# 문자열 양옆의 공백 제거 : strip()
d = """
    안녕하세요.
    문자열의 공백을 제거 하겠습니다
    네네넨.....
"""

print(d.strip())
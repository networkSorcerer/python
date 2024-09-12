# 자연수 A, B, C
# A = 150 , B = 266 , C = 427 이라면 A * B * C = 150 * 266 * 427 = 17037300
# 등장한 숫자 (0 ~ 9) 의 개수를 세는 문제 :
#문자 열로 만들고 비교 하는거 써보기? 
# 참고
#  각 자리 숫자를 구하기 위해 문자열로 변환
#  digits = [int(digit) for digit in str(number)]
# 범위 기반 for 문 사용, count("찾고자 하는 문자")

# elif pw.find(id) >= 0:  # 비밀 번호를 만들때 id 문자열 값을 포함 # 틀리면 -1


# 사용자로부터 세 정수를 입력 받기
A = int(input("정수 입력 : "))
B = int(input("정수 입력 : "))
C = int(input("정수 입력 : "))

# A * B * C 계산
multi = A * B * C

# 결과를 문자열로 변환하여 각 숫자로 분리
NumToStr = [int(s) for s in str(multi)]
print(NumToStr)

# 0부터 9까지 각 숫자의 개수를 저장할 리스트 초기화
count = [0] * 10

# 각 숫자의 개수 세기
for i in range(len(NumToStr)):  # 범위 수정: len(NumToStr)만큼 반복
    digit = NumToStr[i]  # 현재 숫자
    count[digit] += 1  # 숫자에 해당하는 인덱스의 개수 증가

# 결과 출력
for j in range(10):
    print(f"{j}의 개수: {count[j]}")

a,b,c = map(int, input("정수 입력 : ").split()) # 숫자를 공백 기준으로 입력 받음
ls = str(a * b* c)
for i in range(10) : # 0~ 9
    print(ls.count(str(i)), end ="")
# 실습 2번 : 문자열 반전, 문자열을 입력 받아서 문자열 반전 출력
# ex) ABCDEF => FEDCBA
in_str = input("문자열 입력 : ")
for i in range(len(in_str)-1, -1, -1):
    print(in_str[i], end="")
# reverse_str = in_str[::-1]
# print(reverse_str)
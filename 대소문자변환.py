# 영어 소문자와 대뭄ㄴ자로 이루어진 단어를 입력받은 뒤,
# 대문자는 소문자로 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성하시오
# for 문을 사용
# isLower() : 소문자이면 True, 아니면 False

# 입력받은 단어를 대소문자 변경하여 출력하는 프로그램

# 사용자로부터 단어 입력 받기
word = input("단어를 입력하세요: ")

# 결과를 저장할 문자열 초기화
result = ""

# 각 문자에 대해 대소문자 변환
for char in word:
    if char.islower():  # 소문자이면
        result += char.upper()  # 대문자로 변환하여 추가
    else:  # 대문자이면
        result += char.lower()  # 소문자로 변환하여 추가

# 결과 출력
print("변환된 단어:", result)

rst = ""
for e in input("입력 : "):
    if e.islower():
        rst += e.upper() # rst = rst + e.upper()
    else:
        rst += e.lower()

print(rst)

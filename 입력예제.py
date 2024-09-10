# 사용자 에게 콘솔로 입력을 받아 변수에 대입
# input() 함수를 사용
# input() 함수는 문자 열로 입력을 받음

# print("이름을 입력 하세요  : ", end="")
# name = input("이름을 입력 하세요  : ")
# print(f"당신의 이름은 {name} 입니다. ")

# 정수 타입 으로 변수에 값을 대입 하기 위해서 는 형 변환이 필요
# age = input("나이를 입력 하세요 : ")
# print(int(age) + 10)
#age = int(input("나이를 입력 하세요 : "))
#print(age + 10)
# 이름 , 나이 , 주소, 직업, 성적 (실수 타입)float 를 입력 받아 출력 하기

# name = input("이름을 입력 하세요 : ")
# print(f"당신의 이름은 {name} 입니다.")

# 정수 타입으로 변수에 값을 대입하기 위해서는 형 변환이 필요
# 이름 , 나이 , 주소, 직업, 성적(실수 타입)float 를 입력 받아 출력하기
# name = input ("이름 입력 : ")
# age = int(input("나이를 입력 : "))
# addr = input ("주소를 입력 : ")
# job = input ("직업 입력 : ")
# score = float(input("성적 입력 : "))

# print(f"안녕하세요? \"{name}\"님") # 코드내에서 "" 이게 \" 하나의 "
# print(f"당신의 주소는 {addr}이고 직업은 {job}이고 나이는 {age} 입니다")
# print(f"당신의 성적은 {score:.2f} 입니다")

#국어 영어 수학 과학 성적을 공백 기준으로 입력 받아 총점과 평균 구하기
# kor, eng, mat, scn = map(int, input("성적 입력 : ").split())
# total = kor + eng + mat + scn  # 총점 계산
# average = total / 4  # 평균 계산
#
# print(f"총점 : {total}")
# print(f"평균 : {average:.2f}")  # 평균을 소수점 두 자리까지 출력

# score = list(map(int, input("성적 입력 : ").split()))
# print(f"총점 : {sum(score)}")
# print(f"평균 : {sum(score) / len(score)}") # len 은 요소의 갯수를 구한다

# 24 시간 제로 시간을 : 기준 으로 입력을 받아서 시, 분, 초로 찍는데 12 시간 제로 변환ㄴ
hour, min, sec = map(int, input("시:분:초 :").split(":"))

if hour > 12 :
    hour -= 12 # hour = hour = -12
    print(f"오후 {hour}시 {min}분 {sec}초")
else : 
    print(f"오전 {hour} 시 {min} 분 {sec}초")

# - 연도가 4로 나누어 떨어 진다
# -100으로 나누어 떨어 지면 연도는 윤년이 아니다
# - 400 으로 나누어 떨어 지면 윤년 이다
year = int(input("년도를 입력 하세요 : "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"{year}은 윤년 입니다")
else :
    print(f"{year}은 윤년이 아닙니다")
# 제어 문이란? 조건 문과 반복 문의 의미


num = int(input("정수값 입력 : "))

if num > 100 :
    print(f"{num}은 100보다 커요.")
elif num < 100 :
    print(f"{num}은 100보다 작아요.")
else :
    print(f"{num}은 100과 같아요.")

# 실습 문제
# 성적을 입력 받아서 0 ~ 100 사이가 아니면 성적을 잘못 입력 하였다 고 표기
# 성적이 0 ~ 100 이고,
# 90점 이상 이면 "A"
# 80점 이상 이면 "B"
# 70점 이상 이면 "C"
# 60점 이상 이면 "D"
# 나머지 는 "F"
# 점수 입력 받기
while True:
    try:
        # 점수 입력 받기
        score = int(input("점수를 입력 해 주세요: "))

        # 점수 범위 검사
        if score < 0 or score > 100:
            print("성적을 잘못 입력 하였다. 다시 입력해 주세요.")
            continue  # 잘못된 입력 시 다시 입력받기

        # 점수 범위가 올바르 면 등급 판별
        if score >= 90:
            print("A다")
        elif score >= 80:
            print("B다")
        elif score >= 70:
            print("C다")
        elif score >= 60:
            print("D다")
        else:
            print("F다")

        break  # 성적이 올바르면 반복 종료

    except ValueError:
        print("입력 값이 올바르지 않습니다. 숫자를 입력해 주세요.")

# 세자리 정수를 입력 받아 100의 자리, 10의 자리, 1의 자라로 나누어 담고
# 이 중 가장 큰 수 출력

while True :
    try :
        number = int(input("3자리 수를 입력 하세요 : "))
        check = number/100
        if check <= 0 or check >=10 :
            print("3자리 수가 아닙니다. 다시 입력 하세요")
            continue
        else :
            third = int(number/100)
            second = int((number - (third*100))/10)
            first = int(number - (third*100) - (second *10))

            if third > second :
                if third > first :
                    highNumber = third
                    print(f"가장 큰 수를 가진 자릿 수는 {highNumber}")
                else :
                    highNumber = first
                    print(f"가장 큰 수를 가진 자릿 수는 {highNumber}")
            else :
                if second > first :
                    highNumber = second
                    print(f"가장 큰 수를 가진 자릿 수는 {highNumber}")
                else :
                    highNumber = first
                    print(f"가장 큰 수를 가진 자릿 수는 {highNumber}")
            print(third)
            print(second)
            print(first)
            break
    except ValueError :
        print("잘못된 값 입니다.")


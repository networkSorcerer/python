# exceptions(예외 상황) : 프로 그램 작성후 실행 도중에 발생 하는 여러 가지 상황에 대한 것
# 예외 처리란? 예외 상황이 발생 할 가능성이 높은 코드에서 try ~ exception을 통해 흐름을 변경하는것
# while True :
#     try:
#         file_name = input("파일 이름 입력 : ")
#         score_file = open("1score.txt", "r", encoding="utf8") # 해당 파일이 없으면 에러가 발생하지만 이 경우는 그냥 지나 감.
#         print(score_file.read())
#         score_file.close()
#         break
#     except FileNotFoundError:
#         print("파일이 없습니다. 파일 확인 후 다시 진행하세요.")
from multiprocessing.managers import Value
try:
    print("나눗셈 계산기")
    num1 = int(input("첫 번째 숫자 입력 : "))
    num2 = int(input("두 번째 숫자 입력 : "))
    print(f"{num1} / {num2} = {(num1 / num2) : .2f}")
except ValueError:
    print("숫자만 입력 하세요")
except ZeroDivisionError:
    print("나눗 셈은 0으로 나눌 수 없 습니다.")
else :
    print("정상적 으로 처리 되었 습니다.")
finally:
    print("프로그램 종료.")
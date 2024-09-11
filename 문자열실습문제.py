# 2개의 문자열을 포인터 변수 s 와 k에 , 양의 정수를 정수형 변수
# n에 각각 전달 받아 5 문자열의 뒤 부분의 n 개 문자를 k문자열 앝에 끼워넣는 코드 작성
# 예 ) s : seoul
    # k : korea
    # n : 2
    # result : ulkorea

first = input("첫문자 입력")
back = first[3:]
second= input("두번째 문자 입력")
print(back + second)

s = input("s : " )
k = input("k : ")
n = int(input("n : "))
#print(s[-n:] + k)
pos = len(s) -n
print(s[pos:] + k)
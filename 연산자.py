i = 10
j = 3

# 덧셈
print(i + j)  # 결과: 13

# 뺄셈
print(i - j)  # 결과: 7

# 곱셈
print(i * j)  # 결과: 30

# 나눗셈
print(i / j)  # 결과: 3.3333333333333335

# 몫 연산
print(i // j)  # 결과: 3

# 나머지 연산
print(i % j)  # 결과: 1

# 제곱 연산
print(i ** j)  # 결과: 1000

TAX_RATE = 0.10 # 세율
income = int(input("당신은 수입은 얼마입니까?"))
print(f"당신이 내야 할 세금은 {income * TAX_RATE}")

# 대입 연산자 : 값을 변수에 대입 =
# 대입 연산자 의 종류 : =, +=, -=, *=, /=, %=

num1 = 10
num1 += 2 # num1 = num1 + 2
print(num1) #12
num1 -= 10
print(num1) # 2

num1 *= 2
print(num1) #4

# 비교 연산자 : 두개의 값을 비교해서 참/ 거짓을 만들어 냄
# == 같다, > 왼쪽이 크다, >= 왼쪽이 크거나 같다, <, <=

a = 10
b = 20
print(a > b) # False
print(a < b) # True
print(a == b) # False
print(a >= b) # False
print(a <= b) # True


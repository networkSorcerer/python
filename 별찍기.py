# 입력 5
# *
# **
# ***
# ****
# *****

n = int(input("정수 입력 :"))
for i in range(1,n+1) :
    print("*" * i)
print()

s = int(input("입력 : "))
for i in range(s) :
    for j in range(i +1) :
        print("*", end="")
    print()

# 튜플은 시퀀스 자료형
# 이뮤터블(immtable) : 읽기만 가능
# () 또는 괄호 없으면 튜플
# 패킹과 언패킹 동작을 지원함
person = "장원영" , 20, "서울시 강남구 역삼동" # 패킹(Packing)
print(type(person))

num = 1 # ,를 붙이면 튜플 "," 를 지우면 int
print(type(num))

name, age, addr = person # 언패킹(Unpacking)
print(addr)

def get_person():
    name = "안유진"
    age = 21,
    addr = "대전시 유성구"
    return name , age, addr

info = get_person()
print(info)


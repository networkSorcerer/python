# 회원 가입을 위한 아이디 패스 워드 입력 받기
id = input("아이디 입력 : ")

if len(id) >= 8 :
    pw = input("비밀 번호 입력 : ")
    if len(pw) < 8 or len(pw) > 16:
        print("비밀 번호는 8자리 에서 16자리 사이 여야 합니다.")
    elif pw.find(id) >= 0: # 비밀 번호를 만들때 id 문자열 값을 포함 # 틀리면 -1
        print("비밀 번호에 아이디 를 포함할 수 없습니다.")
    else:
        print(f"아이디 는 {id}")
        print(f"비밀 번호 는 {pw}")
else :
    print("아이디 는 반드시 8자리 이상 이어야 합니다.")

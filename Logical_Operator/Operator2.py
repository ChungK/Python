input_id = input("아이디를 입력해주세요\n")
input_pw = input("비밀번호를 입력해주세요\n")
real_id = "rom"
real_pw = "11"

if real_id == input_id and real_pw == input_pw:
    print("Hello!")
else:
    print("Who are you?")

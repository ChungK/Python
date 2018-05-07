import Module3_login
input_id = input("아이디를 입력해주세요")
if Module3_login.login(input_id):
    print('Hello, '+input_id)
else:
    print('Who are you?')
input_id = input("아이디를 입력해주세요")

def login(_id):
    users = ['Rom', 'Chung']
    for user in users:
        if user == _id:
            return True
    return False


if login(input_id):
    print('Hello, '+input_id)
else:
    print('Who are you?')
input_id = input("아이디를 입력해주세요")
# print(type(in_str))
# real_rom = "rom"
# real_lee = "lee"
# if real_rom == in_str:
#     print("Hello!, rom")
# elif real_lee == in_str:
#     print("Hello, lee")
# else:
#     print("Who are you?")

users = ['Rom', 'Chung']
for user in users:
    if user == input_id:
        print('Hello, ' + user)
        import sys
        sys.exit(   )
print('Who are you?')
in_str = input("아이디를 입력해주세요")
print(type(in_str))
real_rom = "rom"
real_lee = "lee"
if real_rom == in_str:
    print("Hello!, rom")
elif real_lee == in_str:
    print("Hello, lee")
else:
    print("Who are you?")

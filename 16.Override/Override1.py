class C1:
    def m(self):
        return 'parent'
class C2(C1):
    # pass #아무 내용 없어도 class
    def m(self):
        # super().m() #부모 코드 m을 의미
        return super().m() + ' child'

o = C2()
print(o.m())
class c1():
    def c1_m(self):
        print("c1_m")
class c2():
    def c2_m(self):
        print("c2_m")

class c3(c1, c2): #앞 쪽 클래스가 우선수누이가 더 높음
    pass

c = c3()
c.c1_m()
c.c2_m()

print(c3.__mro__)#class 우선순위를 알려줌
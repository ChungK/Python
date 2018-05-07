class Cs:
    count = 0 #Class소속 count 변수 0으로 초기화
    def __init__(self):
        Cs.count = Cs.count + 1
    @classmethod
    def getcount(cls):
        return Cs.count

i1 = Cs()
i2 = Cs()
i3 = Cs()
print(Cs.getcount())
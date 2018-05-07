class C:
    def __init__(self, v):
        self.__value = v#__를 붙이면 밖에서 인스턴스 변수 접근 허락X
    def show(self):
        print(self.__value)


c1 = C(10)
# print(c1.getValue())
# c1.setValue(20)
# print(c1.getValue())
# print(c1.value)
c1.show()
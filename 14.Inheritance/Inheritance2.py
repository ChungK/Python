class Cal(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def add(self):
        return self.v1 + self.v2
    def subtract(self):
        return self.v1 - self.v2
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1
class CalMultifly(Cal):
    def multifly(self):
        return self.v1*self.v2
class CalDivide(CalMultifly):
    def devide(self):
        return self.v1/self.v2
c1 = CalMultifly(10,10)
print(c1.add())
print(c1.multifly())

c2 = CalDivide(20, 10)

print(c2, c2.devide())

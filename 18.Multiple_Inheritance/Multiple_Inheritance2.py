class CalMultifly():
    def multifly(self):
        return self.v1*self.v2
class CalDivide():
    def devide(self):
        return self.v1/self.v2

class Cal(CalMultifly, CalDivide):
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
c = Cal(100, 10)
print(c.add())
print(c.multifly())
print(c.devide())

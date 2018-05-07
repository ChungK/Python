class Cal(object):
    _history = []
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def add(self):
        result = self.v1 + self.v2
        Cal._history.append("add : %d + %d = %d" % (self.v1,self.v2,result))
        return result
    def subtract(self):
        result = self.v1 - self.v2
        Cal._history.append("suttract : %d - %d = %d" % (self.v1, self.v2, result))
        return result
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1
    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)
    def info(self):
        return "Cal => v1 : %d, v2 ; %d" % (self.v1, self.v2)

class CalMultifly(Cal):
    def multifly(self):
        result = self.v1 * self.v2
        Cal._history.append("multifly : %d * %d = %d" % (self.v1, self.v2, result))
        return result
    def info(self):
        return "CalMultifly => %s" %(super().info())
class CalDivide(CalMultifly):
    def devide(self):
        result = self.v1 / self.v2
        Cal._history.append("devide : %d / %d = %d" % (self.v1, self.v2, result))
        return result
    def info(self):
        return "CalDevide => %s" %(super().info())

c0 = Cal(30,60)
print(c0.info())
c1 = CalMultifly(10,10)
print(c1.info())
c2 = CalDivide(20, 10)
print(c2.info())

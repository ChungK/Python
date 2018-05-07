class Cs:
    @staticmethod
    def static_method():
        print('Static method')
    @classmethod
    def class_method(cls): #classmethod는 cls를 가지고 있어야함
        print('Class method')
    def instance_method(self):
        print('Instance method')
i = Cs()
Cs.static_method()
Cs.class_method()
i.instance_method()
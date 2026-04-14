
from Proj6 import Calculator

class Child(Calculator):
    num2 = 600

    def __init__(self):
        Calculator.__init__(self,2,3)

    def autocompleted(self):
        return self.num2 + self.num + self.Summation()

obj = Child()
print(obj.autocompleted())


class Calculator:
    num = 100 #Class Variable and is a fixed one. Cannot change everytime!

    #Constructor
    def __init__(self,a,b):
        self.firstnumber = a #Instance Variable
        self.secondnumber = b #Instance Variable
        print("I am called automatically when object is created")

    #Method or Function
    def Summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num

#Object- To call the metho
obj = Calculator(5,6)


print(obj.Summation())









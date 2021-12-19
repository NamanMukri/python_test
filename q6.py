class Calculator():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        

    def add(self):
        print(self.num1+self.num2)
    def subtract(self):
        print(self.num1-self.num2)
    def multiply(self):
        print(self.num1*self.num2)
        
    def divide(self):
        print(self.num1//self.num2)


if __name__=="__main__":
    obj1=Calculator(20,10)
    obj1.add()
    obj1.subtract()
    obj1.multiply()
    obj1.divide()
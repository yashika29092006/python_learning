class Calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+ self.b)
    def sub(self):
        print(self.a-self.b)
    def multiply(self):
        print(self.a*self.b)
    def divide(self,a,b):
        print(self.a/self.b)

cal = Calculator(5,6)
cal.add()
cal.sub()
    
    
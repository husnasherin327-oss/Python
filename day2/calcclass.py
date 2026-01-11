class Calculator():
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b       
    def div(self,a,b):
        if b!=0:
            return a/b
        else:
            return "error"
calc = Calculator()

print(calc.add(10, 5))       
print(calc.sub(10, 5))   
print(calc.mul(10, 5))   
print(calc.div(10, 5))     
print(calc.div(10, 0))        

        
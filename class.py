class sum:
        def __init__(self,num1,num2):
                self.n1=num1
                self.n2=num2
        def addition(self):
                result=self.n1 + self.n2
                print("Addition is",result)
x=sum(100,200)
x.addition()
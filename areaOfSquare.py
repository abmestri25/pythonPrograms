class square:
    def __init__(self,side):
        self.s=side
    def areaOfSquare(self):
        result=self.s *self.s
        print("Area of square is",result)
class rectangle(square):
    def __init__(self,length,breadth):
        square.__init__(self,20)
        self.l=length
        self.b=breadth
    def areaOfRect(self):
        result=self.l * self.b
        print("Area of Rectangle is",result)
x=rectangle(10,20)
x.areaOfSquare()
x.areaOfRect()
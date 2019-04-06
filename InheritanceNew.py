#to avoid unncessesary repeatation of code..we use inheritance

class Person:  #parent class
    def __init__(self,fname,lname): #parent constructor
        self.firstName=fname  #variable initiolization
        self.lastName=lname    #variable initiolization
    def displayName(self):  #function 
        print("First name is ",self.firstName)
        print("Last name is ",self.lastName)

class Year(Person):
    def __init__(self,year):
        Person.__init__(self,"Abhi","Mestri")
        self.graduationYear=year
    def displayGy(self):
        print("Graduation Year is",self.graduationYear)

class Marks(Year):
    def __init__(self,m1,m2,m3,m4):
        Year.__init__(self,"2019")
        self.sub1=m1
        self.sub2=m2
        self.sub3=m3
        self.sub4=m4
    def TotalMarks(self):
        self.totalMarks=self.sub1 + self.sub2 + self.sub3 + self.sub4
        print("Total Marks are ",self.totalMarks)

class Student(Marks):  #chiild class of parent
    def __init__(self,rn):  #child Constructor
        Marks.__init__(self,10,20,30,40)
        self.rollNumber=rn
    def displayRn(self):
        print("Roll Number is ",self.rollNumber)


d=Student("24")  #object of child student class 
d.displayName()     #function calling
d.displayRn()
d.displayGy()
d.TotalMarks()
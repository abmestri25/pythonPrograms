#fibbonacci series means first number will be zero
#second number will be one
#next consecutive numbers will be sum of previous numbers

n=int(input("Enter Number :"))
first=0
second=1
next=0
for i in range(n):
    if(i<=1):  #this will print zero as first number    
        next=i
    else:
        next=first + second
        first=second
        second=next
    print(next)



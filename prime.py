n=int(input("Enter number : "))

#logic goes here
flag=0
for i in range (2,n):
    if(n%i==0):
        flag=1 
        break

if(n==1):#this should not be include in for loop
    print("1 is neither prime nor composite number")

elif(flag==0):
    print("Number is prime")
else:
    print("Number is not prime")

    

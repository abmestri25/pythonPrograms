#program to check whether given number is armstrong or not
x=int(input("Enter no to check :"))
sum=0
t=x
while(x!=0):
    d=int(x%10) #to seperate digits
    sum+=d**3 #sum of cube of seperated digit
    x=x/10 #to seperate original number again
if(sum==t):
    print("Number is armstrong")
else:
    print("Number is not armstrong")
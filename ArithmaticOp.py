n1=int(input("Enter Numerator\n"))
n2=int(input("Enter Denominator\n"))
try:
    result=n1/n2
except:
    print("Denominator must be non-zero")
else:
    print("Result of Division is",result)
finally:
    result=n1*n2
    print("Result of Multiplication is",result)

    result=n1+n2
    print("Result of Addition is",result)

    result=n1-n2
    print("Result of Subtraction is",result)

    
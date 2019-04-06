while True:
    n=int(input("Enter Numerator\n"))
    d=int(input("Enter Denominator\n"))
    try:
        r=n/d
    except:
        print("Denominator must be non-zero")
    else:
        print("Result is",r)
    finally:
        print("End of program")
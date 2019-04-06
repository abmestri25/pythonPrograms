file=open("file.txt", "a")
file.write("Welcome To RMCET\n")
file=open("file.txt","r")
lc=0
uc=0
bc=0
for i in file:
    print(i)
    for j in i:
        if j.islower():
            lc+=1
        elif j.isupper():
            uc+=1
        elif j.isspace():
            bc+=1
print("Lowercase letter count is:",lc)
print("Uppercase letter count is:",uc)
print("Blankspace count is:",bc)
file=open("file.txt", "a")
file.write("Welcome To RMCET\n")
file=open("file.txt","r")
count=0
ele=input("Enter character to search\n")
for i in file:
    for j in i:
        if ele==j:
            count+=1
        else:
            pass
print("Count is",count)
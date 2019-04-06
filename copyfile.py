file=open("file.txt","a")  #file is created

file.write("Welcome To Computer Department\n")
file=open("file.txt","r")  #open it to read mode
newFile=open("newFile.txt","a")  #new file created
for i in file:   #to copy text from one file to another
    print("file.txt content")
    print(i)
    print("newFile.txt content")
    for j in i:
        newFile.write(j)
newFile=open("newFile.txt","r")
print(newFile.read())

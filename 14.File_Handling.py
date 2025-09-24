#types of read
#1. read()
# file=open("student.txt","r")
# content=file.read()
# print(content)
# file.close()0

#2.readline()
# file=open("student.txt","r")
# content=file.readline()  #1st line
# content1=file.readline() #2nd line
# content2=file.readline() #3rd line
# content3=file.readline() #4th line
# print(content)
# print(content1)
# print(content2)
# print(content3)

#3.readlines()

#types of write
file=open("Student.txt","w")
file.write("Hello Hehe\n")
file.write("Hello Python\n")
lines= ["Hello Deeksh\n", "Hello Bunny\n", "Hello World\n", "Hello Python\n"]
file.writelines(lines)
file.close()
def greet(name, branch): #function name
    print("Hello World1",name,branch)
greet("Deeksh","CseAI&ML") #calling function

#argument
def greet(name):
    print("hello",name)
greet("Deeksh")

name="Deeksh"
print("hello",name)

#TYPES functional arg
#A. positional arg
def greet(rollno,name):
    print("Hello", name,"your rollno is", rollno)
greet("E2","Deeksh")

#B.keyword argument
def greet(rollno,name):
    print("Hello", name,"your rollno is", rollno)
greet(name="Deeksh", rollno="E2")

#C.default arg
def greet(name="Student"):
    print("Hello",name)
greet()
greet(name="Deeksh")

#D.variable length
#L=10,20,30,40,50
def sum1(*List1):
    sum2=0
    for i in range(len(List1)):
        sum2=sum2+List1[i]
    print(sum2)
sum1(10,20,30,40,50)

#kwargs
def details(**info):
    for key, value in info.items():
        print(key,"=",value)
details(Name="Deeksh", Rollno="E2", Branch="CSM")

#scope of the variable:

x=10 #global value
def var1():
    x=5
    print("inside var1 function",x,)
var1()
def var2():
    print("inside var2 function", x,)
var2()

print("outside function",x,)


#normal function
def sqe(a):
    print(a*a)
sqe(5)

#lambda function
squ=lambda x:x*x
print(squ(5))
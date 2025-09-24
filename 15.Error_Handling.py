# #error handling

# #1. ZeroDivisionError

# try:
#     a=int(input("Enter numerator: "))
#     b=int(input("Enter denominator: "))
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print("Error: Division by zero is not possible")

# try:
#     a=int(input("Enter numerator: "))
#     b=int(input("Enter denominator: "))
#     c=a//b
#     print(c)
# except ZeroDivisionError:
#     print("Error: Division by zero is not possible")

# try:
#     a=int(input("Enter numerator: "))
#     b=int(input("Enter denominator: "))
#     c=a%b
#     print(c)
# except ZeroDivisionError:
#     print("Error: Division by zero is not possible")


# try:
#     i=2
#     n= int(input("Enter the n value: "))
#     if i%n==0:
#         print("Yes,n is multiple of",n)
#     else:
#         print("no,number is not multiple of",n)
# except ZeroDivisionError:
#     print("Error: Division by zero is not possible")

#ValueError
# try:
#     rollno=int(input("Enter your rollno: "))
# except ValueError:
#     print("Error:given value is not integer data type")

#IndexError
# try:
#     List=[10,20,30]
#     print(List[5])
# except IndexError:
#     print("Error: the given value is not from the list")

# try:
#     List=[10,20,30]
#     n= int(input("entre the index value: "))
#     print(List[n])
# except:
#     print("Error: the given value is not from the list")

#KeyError
# try:
#     Dict= {"name":"Deeks", "Rollno":"E2"}
#     print(Dict["age"])
# except KeyError:
#     print("Error: the given key is not from the list")

#TypeError
# try:
#     List=[10,20,30]
#     Sum= List+5
#     print(Sum)
# except TypeError:
#     print("Invalid type operation")

# try:
#     Sum= "5"+5
#     print(Sum)
# except TypeError:
#     print("Invalid type operation")

#NameError
try:
    print(Mult)
except NameError:
    print("Variable not declared")

#FileNOtFoundError
try:
    file= open("detail.txt","r")
    print(file.read())
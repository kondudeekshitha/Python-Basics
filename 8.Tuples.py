my_tuple=(10,20,30)
print(my_tuple)
print(type(my_tuple))

a= 10
b=[10]
c=(10,)
my_tuple=(10,20,30)
print(type(a))
print(type(b))
print(type(c))
print(type(my_tuple))

#accessing elements
A=(10,20,30,40)
print(A[0])
print(A[1])
print(A[2])
print(A[3])
print(A[-1])
print(A[-2])
print(A[-3])
print(A[-4])

#slicing
A=(10,20,30,40)
print(A[1:3])
print(A[:5])
print(A[0:2])
print(A[-3:-1])

#changing the values
#cant directly change anything

#length
print(len(A))

#maximum
print(max(A))

#minimum
print(min(A))

#sum
sum=0
for i in A:
    sum+=i
print(sum)

#searching and checking
a= (2,4,6,8,10,12,14)
print(3 in a)
if 9 in a:
    print("yes, item is in the list")
if 9 not in a:
    print("no,item is not in the list")

#index()
print(a.index(10))

#count()
print(a.count(10))

#copying
X=["A","A","B","C","A","D"]
Y=X.copy()
print(Y)

Y=X.copy()
Y[3]="D"
print(Y)
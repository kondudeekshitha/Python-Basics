#collection data types
numbers= [10,20,30,40,50]
print(numbers)

fruits=["apple","orange","mango"]
print(fruits)

list1=[10.1,20.5,30.3,40,4]
print(list1)

list2= [True, False, True, True, False]
print(list2)

list3=[10,20,4,"hello", True]
print(list3)

#index
list4=[10,20,30,40,50]
print(list4[2])
print(list4[-1])
print(list4[1:5])
print(list4[-4:3])

slc=["prabhas", "pspk", "bob", "balayya", "bhai"]
print(slc[1:3])
print(slc[1:4])
print(slc[-4:2])


#adding
kalkiCast=["prabhas", "kamal h", "amithab bachchan", "deepika p", "ssr"]
kalkiCast.append("disha p")
print(kalkiCast)

kalkiCast.insert(3,"brammi")
print(kalkiCast)




#remove
kalkiCast.remove("deepika p")
print(kalkiCast)

kalkiCast=["prabhas", "kamal h", "amithab bachchan", "deepika p", "ssr", "deepika p"]
kalkiCast.remove("deepika p")
print(kalkiCast)

kalkiCast=["prabhas", "kamal h", "amithab bachchan", "deepika p", "ssr"]
Cast=["vijay d", "mrunal t",  "disha p", "brammi"]
kalkiCast.extend(Cast)
print(kalkiCast)

#remove
kalkiCast=['prabhas', 'kamal h', 'amithab bachchan', 'deepika p', 'ssr', 'vijay d', 'mrunal t', 'disha p', 'brammi']
kalkiCast.pop(6)
print(kalkiCast)

kalkiCast.pop(6)
print(kalkiCast)

kalkiCast.clear()
print(kalkiCast)

#changing
kalkiCast=['prabhas', 'kamal h', 'amithab bachchan', 'deepika p', 'ssr', 'vijay d', 'mrunal t', 'disha p', 'brammi']
kalkiCast[1]="sundeep r v"
print(kalkiCast)

#mathematical operations in list
#(i) concatenation
a=[1,2]
b=[3,4]
c=a+b
print(c)
#(ii) repetation
#a=[1,2]
#n= int(input("enter n value"))
#b= a * n
#print(b)

#searching and checking.
a= [2,4,6,8,10,12,14]
print(3 in a)
if 9 in a:
    print("yes, item is in the list")
if 9 not in a:
    print("no,item is not in the list")

#index()
print(a.index(8))

#count()
print(a.count(8))

a= [2,4,6,8,8,8,10,12,14]
cnt = 0
for i in range(10):
    if i == 8:
        cnt = cnt + 1

print(cnt)

#sorting
st= [25,12,5,31,13,18,7,45,8,55,68]
st.reverse()#only flips last numbers to first and first numbers to last
print(st)

st.sort() #ascending
print(st)

st.reverse()#descending
print(st)

st.reverse()#again flips to ascending order
print(st)

#copying the list
frnd1=["A","A","B","C","D","A","C"]
frnd2=frnd1.copy()
print(frnd2)

frnd2=frnd1.copy()
frnd2[2]="C"
print(frnd2)

#built-in functions with loops
print(len(frnd1)) #tells the number for items present
print(max(frnd1))#maximum repeated number
print(min(frnd1))#minimum repeated number

s=[3,4,5,6,7,8]
print(sum(s))

o=["apple", "ball","cat"]
print(len(o))

c="hello world"
b=c.split()
print(b)

#a=input("enter the multiple values")
#print(a)

#traversing a list
cars= ["thar","jaguar","audi","bmw"]
for car in cars:
    print("cars=",car)

#using index with for loop
a= len(cars)
for i in range(0,a):
    print("cars",i,cars[i])

#adding elements using for loop
#list1=[]
#n=int(input("enter the numbers of the list value: "))
#for i in range(0,n):
#    a=input(" enter the list value:")
#    list1.append(a)
#print(list1)

#list2=[]
#n=int(input("enter the numbers of the list value: "))
#for i in range(0,n):
#    a=input(" enter the list value:")
#    list1.append(i)
#print(list2)

#list3=[]
#n=int(input("enter the numbers of the list value: "))
#for i in range(0,n):
#    a=input(" enter the list value:")
#    list3.append(i)#
#print(list3)

#sum of list items= 10 20 30 40 50 without using sum()
list=[10,20,30,40,50]
sum=0
for i in [10,20,30,40,50]:
    sum=sum+i
print(sum)

list=[10,20,30,40,50]
sum=1
for i in [10,20,30,40,50]:
    sum=sum*i
print(sum)

#convert=["p","y","t","h","o","n"] to python
p=["p","y","t","h","o","n"]
q="".join(p)
print(q)

r="p"+"y"+"t"+"h"+"o"+"n"
print(r)

list=["p","y","t","h","o","n"]
word = ""
for i in list:
    word=word+i
print(word)

#find maximum and minimum numbers from list without using max() and min()
m=[7,18,12,31,45,17,10,23,229,227]
m.sort()
print(m)

#also without using sort()
list=[7,18,12,31,45,17,10,23,229,227]
max=list[0]
min=list[0]
for num in list:
    if num>max:
        max=num
    if num<min:
        min=num
print(max)
print(min)

#searching and checking
#names=["malla reddy","revanth reddy", "modi","rahul gandhi"]
#searching_names = input ("enter the name to be found: ")
#found=False
#for i in names:
##        found= True

#if found:
#    print("yes")
#else:
#    print("no")

#count even and odd numbers
nums= [7,10,12,17,18,23,31,45,227,229]

evn_cnt=0
odd_cnt=0

for i in range(len(numbers)):
    if nums[i]%2 == 0:
        evn_cnt +=1
    else:
        odd_cnt +=1

print("number of even numbers are: ",evn_cnt)
print("number of odd numbers are: ",odd_cnt)

#reverse the list without using reverse
list1= [7,10,12,17,18,23,31,45,227,229]
l=len(list1)
r_list=[]
for i in range (1-1,-1,-1):
    r_list.append(list[i])
print(r_list)

#remove all negative numbers using loop
list2=[-56,- 9,2,-8,-30,30,45,23,-19,72,-55,-18,7]

pos_list=[]

for i in range(len(list2)):
    if list2[i]>=0:
        pos_list.append(list2[i])

print(pos_list)

#multiply each element in the list
numbers=[56,9,2,8,30,45,23,19,72,55,19,7]
m= int(input("enter the numbers to tbe multiplied: "))
after_multiplication=[]
for i in numbers:
    after_multiplication.append(i*m)
print(after_multiplication)






#write a program to find the average of all numbers in a list
num= [1,2,3,4,5,6]
sum=0
for i in num:
    sum+=i
print(sum/len(num))

#count how many +ve , -ve and zero values a list
#nums=[-5, 0, 8 -9,6,-3,1,5,33,15,-91,-55]


#remove all duplicate elements from a list


#write a program to separate even and odd numbers into two new lists
nums=[1,2,3,4,5,6,7,8,9,0]
even_num=[]
odd_num=[]
for i in nums:
    if nums%2==0:
        even_num.append(nums)
    else:
        odd_num.append(nums)
print(even_num)
print(odd_num)
#take a list of names and print the longest name.
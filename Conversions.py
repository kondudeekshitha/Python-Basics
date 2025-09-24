#leap year or not
year= int(input("enter year:"))
if (year%4==0 and year%100!=0) or year%400==0:
    print("leap year")
else:
    print("not a leap year")
#eligiblity criteria
age=int(input("enter your age"))
if age>=18:
    print("eligible")
else:
    print("not eligible")
#find if the number is even or odd
#even= 0,2,4,6,8,.........
#odd=1,3,5,7,9,.......
num= int(input("enter num :"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")
num= int(input("enter num value:"))
if num%2==0:
    print("even")
else:
    print("odd")
#m->km
distance= 25#m
km= distance/1000
print(km)
#km->m
distance=10#km
m=distance*1000
print(m)
#m->cm
distance=30
cm=distance*100
print(cm)


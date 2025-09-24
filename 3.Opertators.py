#membership operator
text=[1,2,3,4]
print(4 in text)
print(5 in text)
print(4 is not in text)
print(5 is not in text)

#arithmatic operators
a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)
#Logical operator
p=5
q=10
print(p>2 and q<5)
print(p>2 and q>5)
print(p<2 and q>5)
print(p<2 and q<5)
print(p>2 or q>5)
print(q>2 or q<5)
print(p<2 or q>5)
print(p<2 or q<5)
print(not(p>2))
print(not(q>20))
print(10 or 5)
print(5 and 10)
#assignment operator
x=5
x+=5
print(x)
y=10
y**=2
print(y)
y//=2
print(y)
#bitwise operator
x=5
y=3
print(x & y)
print(a | b )
print(~x)
print(a^b)
print(a<<b)
print(a>>b)

#assignemt operators

x=78
print(x)

x=12
x+=3
print(x)#12+3=x

x=10
x-=5
print(x)

x=5
x*=10
print(x)

x=10
x**=2 #exponent (10^2)
print(x)

x=100
x%=6 #reminder
print(x)

x=10
x//=3 #quotient (answer)
print(x)

x=50
x//=4
print(x)

x=5
x&=3
print(x)

#operator logical
x=10
print(x>5 or x<20)
#true


x=5
print(x>3 or x<6)#true


x=10
print(x>8 and x>20)#false

x=100
y=200
print(x>y and x<y)#false

x=5
print(not(x>6))#true

x=10
print(not(x<20))#true

x=100
y=200
print(not(x<y))#false
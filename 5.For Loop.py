#for variable in seq:
#   code block
#range syntax: (start value, end value)
for i in range(1,5,1):
    print("Hello")
for i in range(5,51,5):
    print(i)
for i in range(0,21,2):
    print(i)
for i in range(1,21,2):
    print(i)
for i in range(10,1,-1):
    print(i)
for i in range(16):
    print(i)
for i in range(9,28):
    print(i)
for i in range(1,10,2):
    print(i)
for i in range(1,6,1):
    print(i)

#print squares of a number upto 6
for i in range(1,101):
    print(i*i) #squares


fruits= ["apple", "mango", "orange"]
for x in fruits:
    print(x)

fruit="apple"
for i in fruit:
    if i== "p":
        i.upper()
    print(i)
else:
    print(i)


for i in range(5,51,5):
    print(i)
for i in range(1,11):
    print("5 x ", i , "=", i*5)
for i in range(1,11):
    print("7 x ", i, "=", i*7)

total_sum=0
for i in range(1,26):
    total_sum+=i
    print(total_sum)

for i in range(1,10):
    if i==6:
        break
    else:
        print(i)

for i in range(1,10):
    if i==6:
        continue
    else:
        print(i)

for i in range(1,10):
    if i%2==0:
        pass
    else:
        print(i)

for i in range(0,10):
    if i%2==1:
        pass
    else:
        print(i)

for i in range(1,10):
    if i==4:
        continue
    else:
        print(i)

#arrays in python

#creating an array
import array as arr

Numbers=arr.array('i',[1,2,3,4,5])
print(Numbers)
print(type(Numbers))

#adding an element in array
#append
Numbers.append(7)
print(Numbers)

#inserting
Numbers.insert(2,6)
print(Numbers)

#extend()
Numbers.extend([8,9])
print((Numbers))

#deleting
#pop()
Numbers.pop()
print(Numbers)

#remove
Numbers.remove(2)
print(Numbers)

#update
Numbers[0]=10
print(Numbers)

#looping through arrays:
for i in Numbers:
    print(i)

#basic operations.
#len()
print(len(Numbers))
print(max(Numbers))
print(min(Numbers))
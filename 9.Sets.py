#Sets
a={1,3,5,1,3,5,1,3,5}
print(a)

#empty set
b={}
c=set()
print(c)
print(type(c))


#accessing sets
A={"rajini kanth","snake king","upendra"}
for role in A:
    print(role)

#adding an element in sets.
s={12,18,20}
s.add(25) #adds only single elements in any position
s.update([34,29]) #adds the multiple values in the set
print(s)

#deleting
s.remove(25)
print(s)

#discarding
s.discard(30)
print(s)

#pop
s.pop()
print(s)

#clear
s.clear()
print(s)

#union
a={1,2,3}
b={4,5,6}
print(a|b)

#intersection
c={1,2,3,4}
d={3,4,5,6}
print(c&d)

#difference
print(c-d)
print(d-c)

#symmetric difference


#length
s={12,14,45,18,20}
print(len(s))

#max()
print(max(s))

#min
print(min(s))


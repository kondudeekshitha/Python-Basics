#syntax
Dict= {
    "key1":"value1",
    "key2":"value2",
    "key3":"value3",
    "key4":"value4"
}
print(Dict)

#key value pairs
#unique pairs
A={"n":"Deekshitha","n":"Ashi"}
print(A)

A={"n":"Deekshitha","n1":"Ashi"}
print(A)

B={
    1:"value1",
    20.3:"value2",
    "key":"value3"
}
print(B)

#CREATING DICTIONARY
#normal
Bio_Data={
    "name":"Deekshitha",
    "Rollno":"E2",
    "Branch":"csm",
    "Place":"Hyd"
}
print(Bio_Data)
#empty dict
e_d={}
print(e_d)

#accessing the dictionary
#using[]
print(Bio_Data["name"])
# print(Bio_Data["age"])      [error]

#using get()
print(Bio_Data.get("name"))
print(Bio_Data.get("age"))  #[none]

#adding dict
Bio_Data["age"]=18
print(Bio_Data)

#updating
Bio_Data["Place"]= "Miyapur"
print(Bio_Data)

#Removing in dict #pop(), popitem()-> removes last inserted value, delete(), clear()
del Bio_Data["Place"]
print(Bio_Data)

#Dictionary methods
#keys-> LHS elements; #values-> RHS elements; items-> both LHS & RHS
print(Bio_Data.keys())
print(Bio_Data.values())
print(Bio_Data.items())

#updating multiple values
Bio_Data.update({"Role":"Web developer", "Gender":"Female"})
print(Bio_Data)

#loops for dict
L=[10,20,30,40,50]
for i in range (0,5):
    print(L[i])


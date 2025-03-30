'''
Here we will discuss about the abstruct datatypes in python.
Now what are those? Like --> List, tuples, Set, Dictionaries
'''

a = [1,"Ratul",True,3.54]
b = (1,"Ratul",True,3.54)
c = {1,"Ratul",True,3.54}
d = {"Number": 1,"Name": "Ratul","Value": True, "Decimal": 3.54}

print(a)
print(b)
print(c)
print(d)

# Just like string you can access the elements of the array:

e = [23,41,11,24,35,67,24,98,20]

for i in e:
    print(i,end=" | ")
print()
for j in range(len(e)):
    print(j,end="  | ")
print()

print(e[2:5]) # will print from 2 to 4 th index
print(e[2:5:1]) # will do the same
print(e[:5])
print(e[5:])
print(e[:5:1]) # will print from 0 to 5 - 1  th index following gap of 1
print(e[5::]) # will print from 5 to len(e)-1 th index following gap of 1


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

a = [2,3,4,5]
b = [7,8,9,10]
print(f"[2,3,4,5] + [7,8,9,10] = {a + b}",end=" and ")
a.extend(b)
print(f"[2,3,4,5].extend([7,8,9,10]) = {a} both same.")

'''
Here we will discuss all the built in methods for list in python with their time complexity

Access & Searching:
+-------------------+--------------+-----------------+
|     Operation     |    Method    | Time Complexity |
+-------------------+--------------+-----------------+
|      Indexing     |    lst[i]    |       O(1)      |
+-------------------+--------------+-----------------+
|      Slicing      |   lst[a:b]   |      O(b-a)     |
+-------------------+--------------+-----------------+
|     Searching     |   x in lst   |       O(n)      |
+-------------------+--------------+-----------------+
| Count occurrences | lst.count(x) |       O(n)      |
+-------------------+--------------+-----------------+
|     Get index     | lst.index(x) |       O(n)      |
+-------------------+--------------+-----------------+
Insertion & Deletion
+----------------+----------------------+----------------------------------------------+
|    Operation   |        Method        |                Time Complexity               |
+----------------+----------------------+----------------------------------------------+
|     Append     |     lst.append(x)    |               O(1) (amortized)               |
+----------------+----------------------+----------------------------------------------+
|     Insert     |   lst.insert(i, x)   |                     O(n)                     |
+----------------+----------------------+----------------------------------------------+
|     Extend     | lst.extend(iterable) | O(k) (where k is the length of the iterable) |
+----------------+----------------------+----------------------------------------------+
| Remove element |     lst.remove(x)    |                     O(n)                     |
+----------------+----------------------+----------------------------------------------+
|    Pop last    |       lst.pop()      |                     O(1)                     |
+----------------+----------------------+----------------------------------------------+
|  Pop arbitrary |      lst.pop(i)      |                     O(n)                     |
+----------------+----------------------+----------------------------------------------+
|  Delete slice  |     del lst[a:b]     |                     O(n)                     |
+----------------+----------------------+----------------------------------------------+
Sorting & Reversing:
+-----------+---------------+-----------------+
| Operation |     Method    | Time Complexity |
+-----------+---------------+-----------------+
|    Sort   |   lst.sort()  |    O(n log n)   |
+-----------+---------------+-----------------+
|   Sorted  |  sorted(lst)  |    O(n log n)   |
+-----------+---------------+-----------------+
|  Reverse  | lst.reverse() |       O(n)      |
+-----------+---------------+-----------------+
Copying & Other Operations:
+--------------------+------------------+-----------------+
|      Operation     |      Method      | Time Complexity |
+--------------------+------------------+-----------------+
|        Copy        |    lst.copy()    |       O(n)      |
+--------------------+------------------+-----------------+
| List comprehension | [x for x in lst] |       O(n)      |
+--------------------+------------------+-----------------+
|       Length       |     len(lst)     |       O(1)      |
+--------------------+------------------+-----------------+
'''

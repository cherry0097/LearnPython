'''
On this file we will discuss about the variables and datatypes present in python.
'''

# To print someting:
print("Hellow World")

# To declear a variable you can run the command:

x = 5
y = 6
print(x, y)

# Also you can assign valus like this:

d,e,f = "Hello",45,[12,35,5]

# You can try this as well:
g = h = i = 45
print(f"After update:{[g,h,i]}")
i = 34
print(f"After update:{[g,h,i]}")

'''
Here on the bellow example we can explain about global and local veriables.

By default j = "awesome" is global veriable and j = "fantastic" is the local variable for the function myfunc. So, there are no exsistance of j = "fantastic" outside of the function.

However, if we could mention gloabl j inside the function then we could make it a global veriable. Like we have done it with k.

'''

j = "awesome"
k = "awesome again"

def myfunc():
  global k
  j = "fantastic"
  k = "fantastic again"
  print("Python is local " + j)
  print("Pyhon is global " + k)

myfunc()
# k = "awesome again"
print("Python is " + j)
print("Python is " + k)

"""
Python datatypes:
=================

0. Text Type:	str
1. Numeric Types:	int, float, complex
2. Sequence Types:	list, tuple, range
3. Mapping Type:	dict
4. Set Types:	set, frozenset
5. Boolean Type:	bool
6. Binary Types:	bytes, bytearray, memoryview
7. None Type:	NoneType

"""


# In python the datatypes of the variables automatically taken. However, if you want you can define the datatypes by your own:

# This is known as python casting:

z = str(5)
m = int(765.5321) # Now as I have mentioned that I need m as an integer and not as a flote so it will assign the value 765 only to m

print(z,m)

# You have all the right to say that what's the difference? I can't see any difference on the output.

print(f"integer y + integer x = {y + x}") # on this you will receive an output.
# print(f"integer y + string z = {y + z}") # However, on this:
'''
Traceback (most recent call last):
  File "A:\Learning\Python\Variables_Datatypes.py", line 23, in <module>
    print(f"integer y + string z = {y + z}")
                                    ~~^~~
TypeError: unsupported operand type(s) for +: 'int' and 'str'
'''
# Tadaaaa.... Python doesn't suppot the addition of string and integer.

a = True
b = 1
print(f"{type(a)} -> a + {type(b)} -> b = {type(a + b)} -> {a + b}")

# However you can add boolian and integer.

p = [1,2,3,4]
q = [5,6,7,8]

print(f"{type(p)} -> p + {type(q)} -> q = {type(p + q)} -> {p + q}") # This will add 2 arrays and make 1 array.

# Same like int and float can be added.

"""
Here is the list of that:
"""

# str1 + str2 = str1str2
str1,str2 = "Hellow","world"
print(str1 + str2)

#Here is the end for str data types. Here apart from string, string can't be added to anything.

# int + int = int
# int + float = float
# int + complex = complex

print(4 + 3j)

print(("j","c",3,4) + ("r","t")) # set + set = new set with all the valuse added.

# I am not typing all the other type errors as unlike JavaScript it's easy to rember the data types which can't be added togather rather then which can be added togather.







''' 
On this we will learn about python strings.
'''

# Strings in python can the denoted by:

a = "Hello"
b = 'world'
c = """Ratul"""
d = '''Pal'''

# We can add 2 strings like:

e = a + b + " " + c + d
print(e)

# You can also access any character in a string using index notation, similar to an array, where the first character is at index 0. This allows for efficient traversal of a string using a loop.

print(f"The 3rd element of the string: {e} is '{e[3]}'")

# You can check the leangth of the string using:

print(len(e))

# You can check if any element present in the string:

txt = "The best things in life are free!"
print("free" in txt)
print("atulP" not in e)

'''
Slicing Strings:
'''

print("================Slicing Strings==================")

e = "Ratul Pal"

for i in e:
    print(i,end=" | ")
print()
for j in range(len(e)):
    print(j,end=" | ")
print()

'''
R | a | t | u | l |   | P | a | l | 
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 
''' 
# Now to slice:

print(e[1:7]) # -> This will print from index 1 to index 7-1 = 6

print(e[:4])
print(e[6:])

'''
If at the start the value is not mentioned then the default is 0 and if at the end the value is not present then the default is len(string)

In our case: 0 and end is len(e) - 1 = 8

The value can be negetive as well. Like -1 means len(string) - 1
'''

print()
print("-----------Negetive indexing-----------")
print()
for i in e:
    print(i,end="  |  ")
print()
for j in range(len(e)):
    print(j - len(e),end=" |  ")
print()
print()

'''
R  |  a  |  t  |  u  |  l  |     |  P  |  a  |  l  |  
-9 |  -8 |  -7 |  -6 |  -5 |  -4 |  -3 |  -2 |  -1 | 
'''

print(e[-5:-2])

'''
Now there are some methods are there we can apply on the stings.
'''

# You can make the string upper case, Lower case, You can remove space, you can replace anything, :

print(e.upper())
print(e.lower())
print(e.strip())
print(e.replace("R", "B"))


# However, I feel this stuffs kind of useless to learn as most of the time we use python as backend so, we will hardly deal with these kind of methods of stings.

# You can split the string. Now this can be interesting as this converts our strings to an array:
print(e.split(" "))


# Other things like:

print("My name is \"Pikachu\"\nI am a pokemon\n")

# Other important functions are:

print(e.count("l")) # This will return number of l appeared in the string.
print(e.endswith("l")) # This will return true if the string ends with l
print(e.find("atul P")) # This will return true if it finds the string on the main string.
print(e.index("a")) # Will return the index of 1st l on the array.
# Remeber you split the string
f = e.split(" ")
# Now you can join this string:
print("+".join(f))







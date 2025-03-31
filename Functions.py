'''
Here we will discuss how to define the functions in python and what are the built in functions in python:
'''
'''
The 1st type we will discuss about Math built ins:
'''

print("Max and Min")
print()
a = [2,3,4,5,11,1,55]
print(f"a = {a}")
print(f"max(a) = {max(a)}")
print(f"max(a) = {min(a)}")
print()

print("divmod()")
print()
# quotient, reminder = 10 // 3, 10 % 3 --> Instead of this you can use:
quotient, reminder = divmod(10,3)
print(f"divmod(10,3) = 10 // 3, 10 % 3 :: {quotient, reminder}")
print()

print("abs()")
print()
print(f"abs(-34) = |-34| = {abs(-34)}")
print(f"abs(4 + 3j) = |4 + 3j| = {abs(4 + 3j)}")
print()

print("pow()")
print()
print(f"2^3 = {pow(2, 3)}")
print(f"(2^3) % 4 = {pow(2,3,4)}")
print()

print("round()")
print()
print(f"We need 3 digit round figure of {float(22/7)} = {round(float(22/7),3)}")
print(f"round({float(22/7) * 10000}, -4) = {round((float(22/7) * 10000),-4)}")
print()

print("sum()")
print()
a = [1,2,3,4]
print(f"a = {a}")
print(f"sum(a) = {sum(a)}")
print()

'''To read and write a file you can use this.'''

with open("LearnPython.txt", "r") as f:
    content = f.read()

print(content)
with open("LearnPython.txt", "w") as f:
    f.write("Learn Python")

with open("LearnPython.txt", "r") as f:
    content = f.read()

print(content)

'''Now lets discuss about some Iteration builtins'''

a = [13,45,6,23,9,33,24,56]
iterators = iter(a)
print(a)
print(next(iterators))
print(next(iterators))

n = 2
while n < len(a):
    print(next(iterators)) 
    n += 1

colors = ['Red','Green','Blue','Violate','Yellow','Orange','White','Indego','Black']

enumerated_colors = list(enumerate(colors))
enumerated_colors_dict = dict(list(enumerate(colors)))
print(colors)
print(enumerated_colors)
print(enumerated_colors[3][0])
print(enumerated_colors[3][1])
print(enumerated_colors_dict)

numbers = [23,45,6,78,100,12,34,-11,0]
zipped = dict(zip(numbers,colors))
print(zipped)
print(list(reversed(numbers)))
print(list(sorted(numbers)))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = [x for x in numbers if x % 2 != 0]
print(even_numbers)
print(odd_numbers)

squred_numbers = list(map(lambda x: x**2, numbers))
print(squred_numbers)

even_squred_numbers = [y**2 for y in [x for x in numbers if x % 2 == 0] if y > 20]
print(even_squred_numbers)

















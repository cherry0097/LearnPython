'''
On this we will discuss about the operators in python.

Now on you keyboard almost all the symbols are operators in python. LOL.

But littrelly:

! @ # $ % ^ & * () _ - + = | \ } { [ ] : ' " , < > . / ? ~

Have you noticed anyting missing there?

Yes!! --> ` and ;

This 2 we don't use
'''

a = 16
b = 5

print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a // b = {a // b}")
print(f"a % b = {a % b}")
a += b
print(f"Value of a after a += b: {a}")

a =+ b

print(f"Value of a after a =+ b: {a}")

'''
Now we will discuss the most important part: Bitwise operators:
'''

a = 23
b = 25



def decmialtobinary(n):
    operator = ""
    while n > 0:
        operator += str(n % 2)
        n //= 2
        
    for i in operator[::-1]:
        print(i,end=" | ")

# Now we will play with this:

print("Bitwise operators:")
print()

decmialtobinary(a)
print(a)
decmialtobinary(b)
print(b)

c = a & b

print("AND---------------------------")
decmialtobinary(c)
print(c)

print()
decmialtobinary(a)
print(a)
decmialtobinary(b)
print(b)

c = a | b

print("OR----------------------------")
decmialtobinary(c)
print(c)

print()
decmialtobinary(a)
print(a)
decmialtobinary(b)
print(b)

c = a ^ b

print("XOR---------------------------")
decmialtobinary(c)
print(c)

print()
decmialtobinary(a)
print(a)

c = a >> 2

print("Shift 2 place right------------")
decmialtobinary(c)
print(c)

print()
decmialtobinary(a)
print(a)

c = a << 2

print("Shift 2 place left------------")
decmialtobinary(c)
print(c)

print()
decmialtobinary(a)
print(a)

c = ~a

print("Negetive 23 using ~------------")
decmialtobinary(c)
print(c)







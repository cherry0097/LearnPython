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
operator = ""

while a > 0:
    operator += str(a % 2)
    a //= 2
    
print(operator[::-1])
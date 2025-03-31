'''
Here we will discuss about the classes and objects in python
'''
class Employee:
    increment = 1.1
    # 1st we will create a constructor function:
    def __init__(self, fname, lname, salary,increase): #
        self.fname = fname
        self.lname = lname
        self.salary = salary
        # self.increment = increase
    def yearlyIncrease(self):
        self.salary = int(self.salary * self.increment)
        # self.salary = int(self.salary * Employee.increment)


Ratul = Employee('Ratul','Pal',29990,2.3)
Nicolas = Employee('Nicolas','Tesla',30000,3.4)

print(f"Created and employee {Ratul.fname} {Ratul.lname} with salary: {Ratul.salary}")
print(f"Created and employee {Nicolas.fname} {Nicolas.lname} with salary: {Nicolas.salary}")

Ratul.yearlyIncrease()

print(f"Ratul Pal: {Ratul.salary}\nNicolas Tesla: {Nicolas.salary}")

Nicolas.yearlyIncrease()

print(f"Ratul Pal: {Ratul.salary}\nNicolas Tesla: {Nicolas.salary}")

'''
Now here you need to know the concept of self.
Here when we are running self.increment it's trying to search the increment variable on init function 1st. When it was unable to get any such variable on increment then it went to Employee class and found there so took the value from there.
But if it would able to find the increment on the init function then it would took the value from there.

So, to get rid of it and so that it only takes the value under class we can do this: We can replace self.increment to Employee.increment.

So, long story short:

self.increment --> Instance variable if not then class variable.
Employee.increment --> Class variable

'''

# How to check the variables of instances:

print(Ratul.__dict__)
Ratul.increment = 15
print(Ratul.__dict__)
print(Nicolas.__dict__)

# To check the variables of class:

print(Employee.__dict__)



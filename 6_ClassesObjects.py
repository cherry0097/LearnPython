'''
Here we will discuss about the classes and objects in python
'''
class Employee:
    increment = 1.1
    # 1st we will create a constructor function:
    def __init__(self, fname, lname, salary,increase): #
        self.fname = fname
        self._lname = lname # Now it's protected.
        self.__salary = salary # Now salary is a private vaeriable.
        # self.increment = increase
    def yearlyIncrease(self):
        self.salary = int(self.salary * self.increment)
        # self.salary = int(self.salary * Employee.increment)
    @classmethod
    def setIncrement(cls,amount):
        cls.increment = amount
    @staticmethod
    def sum(a,b):
        return a+b
    def __str__(self):
        return f"The Name of the employee is: {self.fname} {self.lname}"


Ratul = Employee('Ratul','Pal',29990,2.3)
Nicolas = Employee('Nicolas','Tesla',30000,3.4)

# print(f"Created and employee {Ratul.fname} {Ratul.lname} with salary: {Ratul.salary}")
# print(f"Created and employee {Nicolas.fname} {Nicolas.lname} with salary: {Nicolas.salary}")

# Ratul.yearlyIncrease()

# print(f"Ratul Pal: {Ratul.salary}\nNicolas Tesla: {Nicolas.salary}")

# Nicolas.yearlyIncrease()

# print(f"Ratul Pal: {Ratul.salary}\nNicolas Tesla: {Nicolas.salary}")

'''
Now here you need to know the concept of self.
Here when we are running self.increment it's trying to search the increment variable on init function 1st. When it was unable to get any such variable on increment then it went to Employee class and found there so took the value from there.
But if it would able to find the increment on the init function then it would took the value from there.

So, to get rid of it and so that it only takes the value under class we can do this: We can replace self.increment to Employee.increment.

self is an instance argument.

So, long story short:

self.increment --> Instance variable if not then class variable.
Employee.increment --> Class variable

'''

# How to check the variables of instances:

# print(Ratul.__dict__)
# # Ratul.increment = 15
# print(Ratul.__dict__)
# print(Nicolas.__dict__)

# To check the variables of class:

# print(Employee.__dict__)

# print(Ratul.salary)

# Employee.setIncrement(2)
# Ratul.yearlyIncrease()
# print(Ratul.salary)

print(Employee.sum(3,4))

class Programmer(Employee):
    def __init__(self, fname, lname, salary, increase, programming_language):
        super().__init__(fname, lname, salary, increase)
        self.programming_language = programming_language

Naruto = Programmer("Naruto","Uzumaki",4000,2,"Python")

print(Naruto.__dict__)

# help(Naruto)
print(str(Naruto))


''' Lets check data classes'''

from dataclasses import dataclass

@dataclass # It creates 3 methods. You can use @dataclass(frozen = True) will prevent to update the variable in class.
class Student:
    # No need to create any __init__() method
    # No need to create any __repr__() method
    # No need to create any __eq__() method
    name:str
    subject:list
    score:list
    percentage:int

Student1 = Student("Ratul",['DSA','OOP','Functions'],[12,33,45],43)








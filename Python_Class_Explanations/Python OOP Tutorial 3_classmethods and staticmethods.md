#### [Python OOP Tutorial 3: classmethods and staticmethods](<https://www.youtube.com/watch?v=rq8cL2XMM5M>)



We are going to learning about the difference between **regular methods**, **class methods**, and **static methods**.

Regular methods in a class automatically take the instance as the first argument and by convention we were calling this **self**. So, if a regular method automatically takes in the instance as the first argument, then how we change this so that it instead automatically takes the class as the first argument. Now to do that, we're going to use class methods, and to turn a regular method into a class method, it's as easy as adding a **decorator** to the top called class method.

```python
class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)
    
    def apply_raise(self): # (By convention with a regular methoid, we called this instance variable self. )
        self.pay = int(self.pay * self.raise_amount)
    
    @classmethod #create a new method here with that class method decorator (if you want to know more about the decorator, find another detailed video. Basically this is altering the functionality of our method to where now we receive the class as our first argument instead of the instance.)
    def set_raise_amt(cls, amount): #set the name of the method is 'set_raise_amt', and it takes the 'cls' and 'amount' (There's a common convention for class variables too, that is cls.)
        # Now witin this set_raise_amt method, we are working with the cls instead of the instance. Let's set our cls variable raise_amount.
        cls.raise_amount = amount # Here we set the cls variable's raise_amount equal to the amount argument that we are accepting from ths method.
        
        ##pass # Here we just put a pass statement here.

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Employee.set_raise_amt(1.06) # We use the set_raise_amt method we just created, it automatically accepts the class, so we don't have to pass that in. Now we can just pass in the amount.

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

emp_1.set_raise_amt(1.07) # We can also use one instance to run the set_raise_amt method, it will change the class variable too and it will influence all instances. But this action doesn't been used often. 

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
```

You can think that the **cls.raise_amount** changed the class variable directly to the amount.

It's the same thing we use **Employee.raise_amount = 1.06**.



##### New alternative constructor to transform strings with hyphens to new instances

```python
class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.set_raise_amt = amount
        
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-') # first we need to split the string and assign the value
new_emp_1 = Employee(first, last, pay) # then based on those values, we would be able to create a new employee by passing in those values and that would run a __init__ method.

print(new_emp_1.email)
print(new_emp_1.pay)
```



We can create an alternative constructor to change this.

```python
class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.set_raise_amt = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) # Becuase we are in the cls method, here we use cls instead of Employee, they are the same thing.
        
        
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1) # Now we use the new method to change it. 

print(new_emp_1.email)
print(new_emp_1.pay)
```





##### Class methods and Static methods

When working with classes, regular methods automatically pass the instance as the first argument and we call that **self**. Class methods automatically pass the class as the first argument and we call that **cls**. Static methods don't pass anything automatically, they don't pass the instance or the class, so really they behave just like regular functions except we include them in our classes because they have some logical connection with the class.

If we want a simple function that would take in a date and return whether or not that was a workday. So, that has a logical connection to our employee class but it doesn't actually depend on any specific instance or class variable. So, we need to make a static method.

```python
class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.set_raise_amt = amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)    
    
    @staticmethod # Use a decorator to make a staticmethod
    def is_workday(day): # Remember static method don't take the instance or the class as the first argument, so we can just pass in the arguments that we want to work with. Here we just make it simplyer, just check whether or not this day falls on a weekday.
        # In python, dates have these weekday methods where Monday is equal to 0 and Sunday is equal to 6, and all the other days in between.
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        
        
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

import datetime # importing the datetime module
my_date = datetime.date(2016, 7, 10) # remember to follow the formate of this example
print(Employee.is_workday(my_date))
```





Test:

```python
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__():


    def fullname():

    def apply_raise():


    @classmethod
    def set_raise_amt():

    @classmethod
    def from_string():

    @staticmethod
    def is_workday():
```


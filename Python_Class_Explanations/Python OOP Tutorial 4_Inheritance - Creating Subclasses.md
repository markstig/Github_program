#### [Python OOP Tutorial 4: Inheritance - Creating Subclasses](https://www.youtube.com/watch?v=RSl87lqOXDE)



Inheritance allows us to inherit attributes and methods from a parent class. This is useful because we can create subclasses and get all the functionality of our parent class and then we can overwrite or add completely new functionality without affecting the parent class in any way.

If we want to create **developers** and **managers**.

We can make the subclass based on the class we have now.

```python
class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@accenture.com'
        
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee): # Add a new class, and use the parenthesis to specify what classes that we want to inherit from.
	pass # now even without any code of its own the developer class will have all of the attributes and methods of our employee class.


dev_1 = Employee('Corey', 'Shcafer', 50000)
dev_2 = Developer('Test', 'User', 60000) # When we instantiate our developers, it first looked in our developer class for our __init__ method, and it's not going to find it within our developer class because it's currently empty, so what python is going to do then is walk up this chain of inheritance until it finds what it's looking for. Now the chain is called the method resolution order.

print(help(Developer)) # Use the help function to find out what's going on here.

print(dev_1.email)
print(dev_2.email)
```



Now Let's customize our subclass a little bit.

```python
class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@accenture.com'
        
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10 # We can just use this to change the raise_amount for the Developer class.

dev_1 = Employee('Corey', 'Shcafer', 50000)
dev_2 = Developer('Test', 'User', 60000) 

print(dev_1.pay)
print(dev_1.apply_raise()) # No Return value, but it is calculated.
print(dev_1.pay)

print(dev_2.pay)
dev_2.apply_raise() # Class Developer is using independent value which is different from its parent class.
print(dev_2.pay) 
```



We can also initiate our subclasses with more information than its parent class.

```python
class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@accenture.com'
        
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10 
    
    # We need to create a new __init__ method for the Developer class, first we need to copy the __init__ method from its parent class, which is Employee class, and then we add another argument for the new class method.
    def __init__(self, first, last, pay, prog_lang):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@accenture.com'
        self.prog_lang = prog_lang

dev_1 = Employee('Corey', 'Shcafer', 50000)
dev_2 = Developer('Test', 'User', 60000, 'Python') 

print(dev_2.prog_lang)
```

But this way is not clean. We want it to be as maintainable as possible. We want the Employee class handle the first name, last name, and pay arguments. 

```python
class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@accenture.com'
        
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
    	super().__init__(first, last, pay) # super().__init__() is going to pass the first, last, and pay to our employee __init__ method and let that class handle those arguments.
    # Here we don't use super().__init__, we use Employee.__init__(self, first, last, pay), it will also work.
    	self.prog_lang = prog_lang # Here we set the Developer to handle the new argument.
        
class Manager(Employee):
    
    def __init__(self, first, last, pay, employees = None): # Set the employees argument's default value is None, employees here is a list.
        super().__init__(first, last, pay)
        if employees is None: 
            self.employees = [] # [] means an empty list
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
          
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
            
        
dev_1 = Employee('Corey', 'Shcafer', 50000)
dev_2 = Developer('Test', 'User', 60000, 'Python') 

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
mgr_1.print_emps()

mgr_1.add_emp(dev_2)
mgr_1.print_emps()
```



Python has these two built-in functions called **isinstance** and **issubclass**.

**isinstance** will tell us if an object is an instance of a class.

**issubclass** will tell us if a class is a subclass of another.

```python
class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@accenture.com'
        
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10
    
    def __init__(self, first, last, pay, prog_lang):
    	super().__init__(first, last, pay)
    	self.prog_lang = prog_lang
        
class Manager(Employee):
    
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None: 
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
          
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
            
        
dev_1 = Employee('Corey', 'Shcafer', 50000)
dev_2 = Developer('Test', 'User', 60000, 'Python') 

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(isinstance(mgr_1, Manager)) # To test if mgr_1 is an instance of the class Manager
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee)) # To test if Developer is a class of Employee
print(issubclass(Manager, Employee))
```




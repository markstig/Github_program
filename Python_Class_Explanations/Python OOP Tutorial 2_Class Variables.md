#### [Python OOP Tutorial 2: Class Variables](<https://www.youtube.com/watch?v=BJ-VvGyQxho>)



Instance variables are used for data that is unique to each instance. So instance variables are these here that are set using the **self** argument that we saw before. 

For example, in the employee class that we created, we set the names, the email, and the pay in our **init** method. Those are set for each instance of the employee that we create.

```python
class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
    	return '{}.{}'.format(self.first, self.last)
    
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
```



While **class variables** are variables that are shared among all instances of a class. 

So while instance variables can be unique for each instance, like our name and email and pay, class variables should be same for each instance.

What kind of data would we want to be shared among all employees? 

Let's say our company gives **annual raises** every year, now the amount change from year to year, but whatever that amount is, it's going to be the same for all employees. So it would be a good candidate for a class variable. 

```python
class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
    	return '{}.{}'.format(self.first, self.last)
    
    def apply_raise(self):
        # self.pay = int(self.pay * raise_amount) we couldn't add the raise_amount directly here, we should add the class name or self first.
       # self.pay = int(self.pay * Employee.raise_amount) # this one is correct
        self.pay = int(self.pay * self.raise_amount)
    
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
```



Now that might be a little confusing to you because if these are class variables, why we can access them from our instance. 

So, let's print out a few lines here to get a better idea of what's going on.

```python
class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
    	return '{}.{}'.format(self.first, self.last)
    
    def apply_raise(self):
        # self.pay = int(self.pay * raise_amount) we couldn't add the raise_amount directly here, we should add the class name or self first.
       # self.pay = int(self.pay * Employee.raise_amount) # this one is correct
        self.pay = int(self.pay * self.raise_amount)
    
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.__dict__)
print(emp_1.__dict__)
```

We can see that we can access this class variable from both our class itself as well as from both instances.

Now what's going on here is that when we try to access an attribute on an instance, it will first check if the instance contains that attribute. And if it doesn't then it will see if the class or any class that it inherits from contains that attribute.

So when we access **raise_amount** from our instances here, they don't actually have that attribute themselves, they're accessing the **class**'s raise_amount attribute.



Now let's check how to change the variables of the class and what it will affect on the instances.

```python
class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)
    
    def apply_raise(self):
    	self.pay = int(self.pay * self.raise_amount)
        
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Here we change the value of the raise_amount from this class
Employee.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# Now we only change the raise_amount in emp_1
Employee.raise_amount = 1.04 # First we have to change this back
emp_1.raise_amount = 1.05

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)        
```

We can think that the instances inherits the raise_amount variable of the class first, if the class change the value of this variable, all the instances will change. But if one instance change the value of this variable which it inherits, it doesn't influence other instances. 



##### Another example of a class variable

This wouldn't really make sense to use **self**

If we wanted to keep track of how many employees that we have, so the number of employees should be the same for all instances of our class.

We can create a variable of the class with the name of **num_of_emps**, it's value is **0** at the beginning.

Then we can do that within the **init** method since **the init method runs every time we create a new employee**. 

Here we add **Employee.num_of_emps += 1**, we use this instead of **self.num_of_emps**, because with the raises it's nice to have that constant class value that can be overwritten per instance if we really need it to be, but in this case there's no use case I can think of where we would want our total number of employees to be different for anyone instance.

```python
class Employee:
    
    raise_amount = 1.04
    num_of_emps = 0 # set the class variable and value it with 0
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1 # in the __init__ method, we add the increment, because this method will run everytime when we add one instance.
        
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
print(Employee.num_of_emps)    # Here we didn't add any instances right now

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(Employee.num_of_emps)    # Here we have added two instances
```


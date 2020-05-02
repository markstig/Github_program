#### [Python OOP Tutorial 5: Special (Magic/Dunder) Methods](<https://www.youtube.com/watch?v=3ohzBxoFHAY>)



We are going to learn special methods that we can use within our classes, some people call these magic methods. These methods allow us to emulate some built-in behavior within python and it's also how we implement operator overloading.

These special methods are always surrounded by **double underscores**, so a lot of people call these double underscores dunder. 



We're going to change some built-in behaviors and operations. 

These s

Special methods are always surrounded by double underscores. 

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

    def __repr__(self): # Recreate this special method.
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

dev_1 = Employee('Corey', 'Shcafer', 50000)
dev_2 = Employee('Test', 'User', 60000)

# def __repr__(self):
#   pass
# def __str__(self):
#   pass


# print( 1 + 2 )
# print( 'a' + 'b' )
# print(dev_1)
# print(repr(dev_1))
# print(str(dev_1))
# print(repr(dev_1.fullname))
# print(repr(dev_1.fullname()))
# print(str(dev_1.fullname))
# print(str(dev_1.fullname()))
# print(dev_1.__repr__())
# print(dev_1.__str__())

print(int.__add__(1,2))
print(str.__add__('a', 'b'))
```



If we want to add two employees together and have the result be their combined salaries. 

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

    def __repr__(self): # Recreate this special method.
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay

dev_1 = Employee('Corey', 'Shcafer', 50000)
dev_2 = Employee('Test', 'User', 60000)

print(dev_1 + dev_2)
```

[Docs for special method name](<https://docs.python.org/3/reference/datamodel.html#special-method-names>)



len()

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

    def __repr__(self): # Recreate this special method.
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, other):
        return self.pay + other.pay
    

dev_1 = Employee('Corey', 'Shcafer', 50000)
dev_2 = Employee('Test', 'User', 60000)
```






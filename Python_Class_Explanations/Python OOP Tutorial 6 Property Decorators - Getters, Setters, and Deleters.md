#### [Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters](<https://www.youtube.com/watch?v=jCzT9XFZ5bw>)

 

We're going to be learning how to use the property decorator, this allows us to give our class attributes getter, setter, and deleter functionality like may have seen in some other languages.



Question: How to change the *self.email* automatically when we change *self.first*?

```python
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@accenture.com'

    def fullname(self): # Everytime we run this, this will ge the latest self.first and self.last
        return '{}.{}'.format(self.first, self.last)

emp_1 = Employee('Mark', 'Li')
emp_1.first = 'Jim' # If we only change it here, the email will not change automatically.


print(emp_1.first)
print(emp_1.email) 
print(emp_1.fullname())
```



We have the ability to do this within Python using the property decorator. Now the property decorator allows us to define a method but we can access it like an attribute.

```python
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last


    def email(self): # It is the same with the fullname method.
        return '{}.{}@accenture.com'.format(self.first, self.last)

    def fullname(self):
        return '{}.{}'.format(self.first, self.last)

emp_1 = Employee('Mark', 'Li')
emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email())
print(emp_1.fullname())
```

In order to continue accessing email like an attribute we can just add a property decorator above this method.

```python
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    # Here we are defining our email in our class like it's a method but we are able to access it like an attribute
    @property
    def email(self):
        return '{}.{}@accenture.com'.format(self.first, self.last)

    # And we could do this just as easily with fullname as well
    @property
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)

emp_1 = Employee('Mark', 'Li')
emp_1.first = 'Jim'

print(emp_1.first)
print(emp_1.email) # If we added the '@property' we should delete the parenthesis here.
print(emp_1.fullname)
```



Show you an example of you can use a setter.

```python
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@accenture.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split('.')
        self.first = first
        self.last = last

emp_1 = Employee('Mark', 'Li')

emp_1.fullname = 'Jay.Zhou'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
```



Show you an example of you can use deleter.

```python
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@accenture.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split('.')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee('Mark', 'Li')

emp_1.fullname = 'Jay.Zhou'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.first, emp_1.last)
```



This is a nice feature because it allows us to access attributes without putting getters and setters everywhere. But if we need that functionality then it's easy to add in with the property decorator. 

If you do this correctly then people using our class won't even need to change any of their code because they'll still be able to access those attributes in the same way that they did before.


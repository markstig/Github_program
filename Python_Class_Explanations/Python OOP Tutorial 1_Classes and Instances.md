#### [Python OOP Tutorial: Classes and Instances](<https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=WL&index=16&t=0s>)


[Need to check out the 'return' functionality](https://www.cnblogs.com/vamei/archive/2012/06/01/2529500.html)

You can see classes being used throughout most moder programming languages.

They allow us to logically group our data and functions in a way that's easy to [reuse] and also easy to build upon if need be.

Just a quick side note: when we talk about data and functions that are associated with a specific class, we call those attributes and methods. So when we say methods, we mean a function that is associated with a class.



```python
class Employee:
    pass
```



A class is basically a blueprint for creating instances and each unique employee that we create using our employee class will be an instance of that class.

```python
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)
```



Instance variables contain Data that is unique to each instance.

Let's say employees have first name, last name, email address, and a payment information.

Each of these instances have attributes that are unique to them.

We can check by printing them out.

```python
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

print(emp_1)
print(emp_2)

emp_1.first = 'Corey'
emp_1.last = 'Schafer'
emp_1.email = 'Corey.Schafer@company.com'
emp_1.pay = 50000

emp_2.first = 'Test'
emp_2.last = 'User'
emp_2.email = 'Test.User@company.com'
emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)
```

But in this way, we have to fill all the employees' information manually, and it definitely will make mistakes.



In order to set up automatically when we create the employee, we're going to use a special init method.

Now inside our employee class we're going to create this special init method. We can think of this method as initialize and if you're coming from another language, then you can think of this as the constructor now when we create methods within a class they [receive] the instance as the first argument automatically. By convention, we should call the instance self, now you can call it whatever you want, but it's a good idea to stick to convention here and just use self.

So after **self** we can specify what other arguments that we want to accept. So let's go ahead and accept the first name, the last name, and the pay. We know that we had email too, but we can create the email using the first name and the last name so now within our init method, we are going to set all of these instance variables.

Whenever we say that **self** is the instance what we mean by that is that when we set **self.first = first** here. It's going to be the same thing  as us saying down that **emp_1.first = 'Corey'**. Except now instead of doing this manually, It'll be done automatically when we create our employee objects.

These don't need to be the same as our arguments, so for example, we could make **self.fname = first** in the **init**, but we usually like to keep these similar if possible.

Now when we create our instances of our employee class right here, now we can pass in the values that we specified in our **init** method, now our **init** method takes the instance which we call **self**, and **first**, **last**, and **pay** as arguments.

But when we create our employee down, the instance is passed automatically so we can leave off **self**, we only need to provide the names and the pay.

So here is what happened to **emp_1 = Employee('Corey', 'Schafer', 50000)**

1. **emp_1** will be passed as **self**
2. Then it will set all of these attributes automatically

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#print(emp_1)
#print(emp_2)

print(emp_1.email)
print(emp_2.email)
```



Now Let's say that we wanted the ability to perform some kind of action.

To do that we can add some method to our class.

If we want the ability to display the full name of an employee. Now this is an action that you'd likely need to do a lot with a class like this.

We can do this manually outside the class, like using the **format**.

But that's a lot to type in each time that we want to display the employees full name.

So we can create a method within our class that allows us to put this functionality in one place.

We can create a method called **fullname**, as we said before, each method within a class, automatically takes the instance as the first argument, we're going to always call that **self**, and the instance is the only argument that we'll need in order to get the full name.

So within the **fullname** method, we're going to take the same logic that we had before like the **format**.

But we have to be careful here because now instead of printing **emp_1** first name and last name, we're going to use **self** so that it will work with all instances.

Now we can use **print(emp_1.fullname)** to print out the full name.

Here we remember we should add the parenthesis, because this is a method instead of an attribute.

```python
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{}.{}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

#print(emp_1)
#print(emp_2)

print(emp_1.email)
print(emp_2.email)

print("{}.{}".format(emp_1.first, emp_1.last))
print(emp_1.fullname)
print(emp_1.fullname())
```



One common mistake is forgetting the **self** argument for the instance.

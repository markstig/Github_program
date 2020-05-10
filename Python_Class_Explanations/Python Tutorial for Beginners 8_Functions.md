#### [Python Tutorial for Beginners 8: Functions](<https://www.youtube.com/watch?v=9Os0o3wzS_I>)



Functions are basically some instructions packaged together that perform a specific task.

```python
def hello_func(): # in the parenthesis we add parameters.
    pass # pass keywords means we don't want to do anything with this for now but it won't throw any errors for leaving it blank.

print(hello_func) # it princts out that this is a function in a certain location and memory, but it didn't execute the function. 
print(hello_func()) # add the parenthesis can run the funciton, but because we're not doing anything with this function yet and it doesn't have a 'return' value, so we'll get 'None'

def hello_func_1():
    return 'This we add the RETURN for this funciton.'
print(hello_func_1()) # Because we add the return value, we'll get the return value when we print this function out.


def hello_func_2():
    print('Hello Function!')
hello_func_2() # We run this function, it will execute it, because in this function we let it print a string ,that's the reason why the string will be printed.

print(hello_func_2()) # Here we didn't add any Return value for this funciton, that's the reason why we get 'None' here.   
```



One benefit of function is that they allow us to reuse code without repeating ourselves.

```python
def hello_func():
    print('Hello, Mark!') # If we use function, we can easily change it and apply the modification automatically.

# hello_func() * 10 We couldn't use * 10 here

hello_func()
hello_func()
hello_func()
hello_func()
hello_func()
```



What doest it mean for our function to return something? 

This is where functions become really powerful because it allows us to operate on some date and then pass the result to whatever called our function. So instead of printing the string hello function within here Let's instead return this. 

```python
def hello_func():
    return 'Hello Function.' # This means when we execute our function it's actually going to be equal to our return value, so these executed functions here are actually equal to the string 'Hello Function'

hello_func() # If we run this, it doesn't give us any result because it just a string that we're not doing anything with.
print(hello_func()) # But we can print this string out.

# In this function, we don't have any input value and the return value is a string.

print(len('Test')) # We don't need to know the code of the len() funciton, we just need to focus on the input and output.

# We can treat the return value just like the data type that it is and understanding this will allow you to chain together some functionality.
# We know our hello function returns a string, so we can treat that executed function just like a string. We can uppercase it.
print(hello_func().upper())
print(hello_func().lower())
print(hello_func() * 10)
print((hello_func() + '\n') * 10)
```

So, basically think of a function as a machine that takes input produces a result. When you execute a function, you can think of it almost like a black box, you don't need to know exactly how it's doing what it's doing, you're mainly concerned about the **input** and the **return** value. 



##### Add arguments

```python
def hello_func(greeting): # We add one argument for this function.
    return '{} Function.'.format(greeting)

print(hello_func('Mark'))

def hello_func_1(greeting, name = 'You'): # We add the default value for the argument of name
    return '{},{}'.format(greeting, name)

print(hello_func_1('hi')) # Even if we didn't input the name argument, it won't give us an error becuase it can use the default value of the name.
print(hello_func_1('Hi','Mark'))
print(hello_func_1('Hi', name = 'Lily'))
```



[More Scope Video ](https://youtu.be/QVdf0LgmICw)



##### *args and *kwargs

The ***args** and **\*\*kwargs**  are allowing us to accept an **arbitrary** number of positional or keyword arguments.

In this example, we don't know how many of these positional or keyword arguments that will be and that's why we use star args and star star kwargs.

The names don't have to be args and kwargs, but that's a convention that you'll see a lot, so it's always good to stick with convention so that people can understand your code.

```python
def student_info(*args, **kwargs): 
    print(args) # It's actually a tuple
    print(kwargs) # It's actually a dict

student_info()

student_info('Math','Art',name = 'John', age = 22) # We add some positional arguments and keywords arguments.

courses = ['Mathmetics', 'Phisics'] # We add a list
info = {'name': 'Mark', 'age': 32} # We add a dict
student_info(courses, info) # In this way, we can only make the input info be shown as one list.
student_info(*courses, **info) # We need to unpack the list and dict by using the * and **
```





##### Test - Leap year and month

```python
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year %400 == 0)

def days_in_month(year, month):
    """Return number of days in that month in that year."""
    if not 1 <= month <= 12:
        return 'Invalid Month'
    if month ==2 and is_leap(year):
        return 29
    return month_days[month]

print(days_in_month(2020,2))
```




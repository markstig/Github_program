#### [Python Tutorial for Beginners 9: Import Modules and Exploring The Standard Library](https://www.youtube.com/watch?v=CqvZ3vGoGs0)



We'll start by importing modules that we've written and then we'll explore a bit of the standard library and how we can import those modules to solve a lot of common problems.

First Create a module named **my_module.py**:

```python
print('Imported my_module...')

test = 'Test String'

def find_index(to_search, target): # two arguments, a list of 'to_search', and a target they are looking for
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
        
    return -1
```



Let's create another code to import the module we set above.

```python
import my_module as mm # To import this module, we need to go up of the file, and write the code like left, before this, we have to make sure the module we are going to import is in the same directory as our test.py.
# We use 'import my_module as mm' to make the name shorter when we use it.

courses = ['History', 'Math', 'Physics', 'CompSci']

index = mm.find_index(courses, 'Math')

print(index)
```



We can also just import the function from the module.

```python
from my_module import find_index as fi # This only give us access to the find_index function and not everyting else in the module, like in this condition, we couldn't use the 'test' variable in the module, if we want to use it we can try this: 'from my_module import find_index as fi, test'. We also can make the find_index shorter as fi.
## We can also do this like: 'from my_module import *', but we had better not do this because if we have problems next, it's hard to track down where it is.

courses = ['History', 'Math', 'Physics', 'CompSci']

index = fi(courses, 'Math') # Attention, this is not readable for others, don't use it like this, try to use it as readable as possible. This is just to show how we can use it conveniently.

print(index)
```



Actually, python use a list called **sys.path** to find where the module is.

```python
import sys

print(sys.path)
```

We can add new path to this.  We can also use windows 'environment variables' to add this. Check this on-line.

```python
import sys
sys.path.append('C:Users\\mark.a.li\\Downloads\\') # Remember to use the double \
print(sys.path)
```



##### Standard Library



random module

```python
import random

courses = ['History', 'Math', 'Physics', 'CompSci']

random_course = random.choice(courses)

print(random_course)
```



math module

```python
import math

rads = math.radians(180) # convert 180 degrees to radians

print(rads)

print(math.sin(rads)) # convert the rads to sin value
print(math.sin(30))
```



datetime module and calendar module

```python
import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2017))
```



os module (This is going to give us access to the underlying operating system)

```python
import os

print(os.getcwd()) # to see the current working directory
```



print the file location

```python
import os

print(os.__file__)
```














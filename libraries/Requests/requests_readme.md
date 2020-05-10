[Python Request Tutorial](https://www.youtube.com/watch?v=iv-Uc8d3tDs)

## What is Python Requests?
Python Requests is a python library used to get requests from the web pages.

## Why use Python Requests?
Do not have to manually add query strings to URLs, or form-encode Post data.

## How to Install Requests?
### You can run the following command in the terminal, if you have installed pipenv.
$ pip install requests
### Use Pycharm or others...

## Making GET Requests
~~~Python
import requests
r = requests.get('url')
# we will have a response object r.
~~~

~~~python
import requests
payload = {'key1': 'value1'}
res = requests.get('https://httpbin.org/get', params=payload)
print(res.url)
~~~


## Making POST Requests
Post request is used to submit the data to be processed to the server.

~~~python
import requests
payload = {key1: value1, key2: value2}
r = requests.post('url', data=payload)
# We will have a respoonse object r.
~~~

~~~python
import requests
payload = {'key1': 'value1'}
res = requests.post('https://httpbin.org/get', data=payload)
print(res.text)
~~~

## Cookies And Headers
We can view the servers headers using a python dictionary and similarly access the cookies in the server as well.

## Session Objects

## Erros and Exceptions







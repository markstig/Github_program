### curl

Httpbin.org is a very useful website for us to learn http realted knowledge.

curl --help (a brief instruction)

man curl (a brochure)

| parameters | instructions                                                 | examples                                                     |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| -A         | set the user agent                                           | curl -A 'Chrome' http://www.baidu.com                        |
| -X         | use specific method to request                               | curl -X POST http://httpbin.org/post                         |
| -I         | only return the **Headers** information                      | curl -I http://baidu.com <br />curl  -I http://www.baidu.com |
| -d         | use the **POST** method request target url, and send some arguments | curl -d test=123 http://httpbin.org/post<br />curl -d "a=1&b=2&c=3" http://httpbin.org/post<br />curl -d a=1 -d b=2 -d c=3 http://httpbin.org/post<br />curl -d @filepathandname http://httpbin.org/post |
| -O         | use the original object name to download the file            | curl -O http://httpbin.org/image/jpeg                        |
| -o         | use a new name to download the file                          | curl -o covid19 https://www.cdc.gov/coronavirus/2019-ncov/downloads/COVID19-symptoms.pdf |
| -L         | follow and relocate the address                              | curl -IL https://baidu.com                                   |
| -H         | setting the header information, use this to get specified content | curl -o image.webp -H 'accept:image/webp' http://httpbin.org/image |
| -k         | ignore ssl certificate                                       | curl -k https://12306.cn                                     |
| -b         | set cookies                                                  | curl -b a=test https://httpbin.org/cookies                   |
| -s         | show simple message                                          |                                                              |
| -v         | show detail message                                          |                                                              |

we can combine **curl** and **regex** to get some data below:

curl http://httpbin.org/get |grep -E '\d+'

alias myip="curl http://httpbin.org/get|grep -E '\d+'|grep -v User-Agent|cut -d '\"' -f4"

### wget

| parameters        | instructions                                                 | examples                                                     |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| -O                | use a new name to download                                   | wget -O 'new.png' http://httpbin.org/image/png               |
| --limit-rate=200k | limit download rate                                          | wget --limit-rate=200k https://xxxxxx.mp4                    |
| -c                | resume download                                              | wget -c --limit-rate=200k https://xxxxxx.mp4                 |
| -b                | Download backgroud                                           | wget -b --limit-rate=200k https://xxxxxx.mp4                 |
| -U                | set user agent                                               | wget-U 'windows IE 10.0' -bc --limit-rate=200k https://xxxx.mp4 |
| --mirror          | mirror target website                                        | wget --mirror -U 'Mozilla' -p http://docs.python-requests.org |
| -p                | download related resources                                   |                                                              |
| -r                | downlaod recursive (if you use mirror, do not need to use this one) |                                                              |
| --convert-links   | convert relative links to absolute links                     |                                                              |

### httpie

like curl

### python -m http.server

a server build in python, use the local folder as a server, if there is an index file, it will show like a website.

127.0.0.1/8000

### urllib

~~~python
from urllib import request

r = request.urlopen('http://httpbin.org/get')
print(dir(r))
print(type(r))

text = r.read()
print(text)

print(text.decode('utf-8'))

print(r.status)
print(r.reason)

print(r.headers)

print(dir(r.headers))

print(r.headers.get_all('content-type'))

print(r.headers.keys())

print(r.headers._headers)
print(dict(r.headers._heades)) # change it to a dic

~~~

~~~python
import urllib.request
import json

r = urllib.request.urlopen('http://httpbin.org/get')

# read the content of the response
text = r.read()
print(text)
# return the status and message
print(r.status, r.reason)
# if the returned content is jason type, we can load it directly
obj = json.loads(text)
print(obj)

# r.headers is a http message object
print(r.headers)
# if we want ot print the object
for k, v in r.headers._headers:
  print('%s: %s'%(k,v))


# Add customized header information
ua = 'Mozilla/5.0' #change the user agent
req = urllib.request.Request('http://httpbin.org/user-agent')
req.add_header('User-Agent', ua)
# receive an object as the argument
r = urllib.request.urlopen(req)
resp = json.load(r)
# print the user-agent info from the messages from httpbin response
print("user-agent: ", resp["user-agent"])

~~~



Some websites want you to provide the username and password.

We can use httpbin to make a test.

If we want to visit the website blow, we must enter the username and password, otherwise, it will show '401', it means you are not authorized to visit:

*httpbin.org/basic-auth/mark/123456* 



**?????????? The following codes still have a problem, waiting  to be solved.**

~~~python
import urllib.request

auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='httpbin auth', uri='/basic-auth/mark/123456', user='mark', passwd='123456')
opener = urllib.request.build_opener(auth_handler)
urllib.request.install_opener(opener)
r = urllib.request.urlopen('http://httpbin.org')
print(r.read().decode('utf-8'))

~~~

~~~python
# use the get 
import urllib.request, urllib.parse # Here we must import .xxxx directly
import json

params = urllib.parse.urlencode({'spam':1, 'eggs':2, 'bacon': 2})
url = 'http://httpbin.org/get?%s'%params
with urllib.request.urlopen(url) as f:  # use with here, we don't need to name an object every time
    print(json.load(f))
~~~

~~~python
# use post to transfer parameters
import urllib.request, urllib.parse # Here we must import .xxxx directly
import json

data = urllib.parse.urlencode({'name':'Mark', 'age':2})
data = data.encode()
with urllib.request.urlopen('http://httpbin.org/post', data) as f:
    print(json.load(f))
~~~

~~~python
# use proxy IP request remote url

import urllib.request, urllib.parse # Here we must import .xxxx directly
import json

proxy_handler = urllib.request.ProxyHandler({'http':'http://iguye.com:41801'})
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler() # This handle username and password
opener = urllib.request.build_opener(proxy_handler)
r = opener.open('http://httpbin.org/ip')
print(r.read())

~~~

~~~python
# urlparse module
import urllib.parse

o = urllib.parse.urlparse('http://httpbin.org')
print(dir(o))
~~~

### requests

~~~python
import requests

# get request
r = requests.get('http://httpbin.org/get')
print(r.status_code)
print(r.reason)
print(r.text)

# get request with parameters
r = requests.get('http://httpbin.org/get', params={'a':'1', 'b':'2'})
print(r.json())

# post
r = requests.get('http://httpbin.org/post', data={'a': '1'})
print(r.json())

# customize headers
ua = 'Mozilla/5.0'
headers = {'User-Agent': ua}
r = requests.get('http://httpbin.org/headers', headers=headers)
print('customized request: ', r.json())

# requests with cookies
cookies = dict(userid='123456', token='----------')
r = requests.get('http://httpbin.org/cookies', cookies=cookies)
print(r.json())

# basic-auth
r = requests.get('http://httpbin.org/basic-auth/mark/123456', auth=('mark', '123456'))
print('Basic auth: ', r.json())

# show abnormal status 
bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
bad_r.raise_for_status()

# session
# set a Session object
s = requests.Session()
# this session object will save the conent of the set cookies
s.get('http://httpbin.org/cookies/set/userid/123456789')
# next request will add the cookies info to the header info automatically
r = s.get('http://httpbin.org/cookies')
print('check the cookies in this Session: ', r.json())

# proxy
print('not use proxy: ', requests.get('http://httpbin.org/ip').json())
print('use proxy: ', requests.get('http://httpbin.org/ip', proxies={'http': 'http://iguye.com:41801'}).json)

# timeout
r = requests.get('http://httpbin.org/delay/3', timeout=10)
print(r.text)
~~~



Ubuntu: apt

Centos: yum -y install tinyproxy ????



# BS4

[Beautiful Soup Documents](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

~~~python
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
  
soup.title
soup.title.name
soup.title.string
soup.title.parent.name
soup.p
soup.p['class']
soup.a
soup.a.attrs
soup.a['class']
soup.a.attrs['class']
soup.find_all('a')
soup.find(id='link3')

for link in soup.find_all('a'):
    print(link.get('href'))  # or we can print(a.attrs['href'])

soup.p.children
list(soup.p.children)
list(soup.p.children)[0]
list(soup.p.children)[0].text

print(soup.get_text())

# 支持css选择器
soup.select('#link1')
soup.select('.story')
soup.select('p.sotry')
~~~

~~~python
# a test of baidu

import requests, bs4, pprint

target = requests.get('https://www.baidu.com')
print(target)

soup = bs4.BeautifulSoup(target.content, 'html.parser')

for i in soup.find_all('a'):
  print(i.text, i['href'])
~~~

~~~python
# A test for login jd search pages, here is only a test

import requests, bs4, pprint

# header we just use the informaiton from the chrome inspectors
headers = {
        'Cookie': 'shshshfpa=828dddb6-9505-dfea-586a-7a6bd86ec22f-1579751643; shshshfpb=rPaeB9GKaQGRbt2DL5H3v%2FA%3D%3D; pinId=L0L47z-UAMBhIyufUIIN9rV9-x-f3wj7; qrsc=3; __jdv=76161171|direct|-|none|-|1584717076217; __jdu=1584717076216460715361; xtest=7128.cf6b6759; rkv=V0600; areaId=2; ipLoc-djd=2-2825-0-0; PCSYCityID=CN_310000_310100_310112; user-key=a5632f67-d505-4726-967b-eaebe8dabb29; pin=jd_7aa45d2b231c5; unick=emisora; _tp=qr3JhPFTJVGV4UOmOgoGiqiaeS6m9m90fth5BpsRyNM%3D; _pst=jd_7aa45d2b231c5; TrackID=1PV29S5ACs6htjTBkCvcBbgEqu8sJkOy5V316tJV_9wzfgqqJgdGGHJFEJm-cQhqxVjMhFova4Ozijbgv_n4bPKWg_ZyRxhMljuCLdouIlIDUHH82jPQk31U7oDFrOYb2; ceshi3.com=000; shshshfp=8e26e4978adbc1dd54d5e886967d1ff9; 3AB9D23F7A4B3C9B=M4MO3FXM2MJOU6XUITONBKDULLURTA3KXD2KZMSPLNJFCVVCYKIBLLS4SYTPNQAJMLTCSY2W5GSVRI6V5K7446EV2Q; _gcl_au=1.1.1351501015.1585292936; cn=0; __jda=122270672.1584717076216460715361.1584717076.1585289009.1585476389.8; __jdc=122270672; shshshsID=879ad7c93f6ba0d8ad5c56e621591441_1_1585476401961; __jdb=122270672.4.1584717076216460715361|8.1585476389; wlfstk_smdl=a3zxegbvnmcymlv45tc1hki3v6d7bbcm',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }

target = requests.get('https://search.jd.com/Search?keyword=%E8%8D%AF&enc=utf-8&suggest=1.rem.0.undefined&wq=%E8%8D%AF&pvid=ed39b0e947ef4ff392984c13832dc5c2', headers = headers)

print(target)


soup = bs4.BeautifulSoup(target.content, 'html.parser')

print(soup)


for i in soup.find_all('a'):
    print(i.text, i['href'])
~~~

### lxml

Use C to write  the lxml, it is faster.

~~~python
from bs4 import BeautifulSoup

import lxml, pprint

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup_lxml = BeautifulSoup(html_doc, 'lxml')
print('##'*10, soup_lxml.a)
~~~

~~~python
from lxml import etree

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

selector = etree.HTML(html_doc)
links = selector.xpath('//p[@class="story"]/a/@href')

for link in links:
    print(link)
~~~

**xpath** is a language which used to find information in XML files.

concepts:

node(节点)

1. 元素

2. 属性
3. 文本
4. 命名空间
5. 文档（根）节点

节点关系

1. parent

2. children

3. sibling

4. ancestor

5. descendant

   

~~~python
from lxml import etree
import requests
import pprint

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

selector = etree.HTML(html_doc.encode('utf-8'))
links = selector.xpath('//p[@class="story"]/a/@href')

for link in links:
    print(link)

print(selector.xpath('//p/text()'))
print(selector.xpath('/html//head/text()'))
print(selector.xpath('//a/text()'))
print(selector.xpath('//a/@href'))

body = selector.xpath('/html//body')
print(body)
print(body[0])

# '.' from the current node
print(body[0].xpath('./p/text()'))
~~~

**xpath grammar**

| expressions | descriptions                          |
| ----------- | ------------------------------------- |
| nodename    | choose all the node's and sub-nodes   |
| //          | choose from any nodes                 |
| /           | only choose from the root node        |
| .           | choose current node                   |
| ..          | choose the current node's parent node |
| @           | choose attributes                     |

## 下厨房

~~~python
from bs4 import BeautifulSoup
import requests
import lxml
import os
from urllib.parse import urlparse
import pprint

r = requests.get('http://www.xiachufang.com/')
soup = BeautifulSoup(r.text, 'lxml')

imgs = soup.select('img')

img_list = []
for img in imgs:
    if img.has_attr('data-src'):
        img_list.append(img.attrs['data-src'])
    else:
        img_list.append(img.attrs['src'])
img_list2 = []
for i in img_list:
    a = i.split('@')
    img_list2.append(a[0])

# create a folder
image_dir = os.path.join('/Users/markli/Downloads', 'images')
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)


for img in img_list2:
    o = urlparse(img)
    if '/' in o.path[1:]:
        opath = o.path[1:].replace('/', '_')
    else:
        opath = o.path[1:]
    filepath = os.path.join(image_dir, opath)
    resp = requests.get(img)
    with open(filepath, 'wb') as f:
        for chunk in resp.iter_content(1024):
            f.write(chunk)
        f.close()
~~~

~~~python
# use crul and regex

import os
import re
from io import BytesIO
from urllib.parse import urlparse
import pycurl
import pprint

# create a buffer object, use curl to write the contents to this buffer
buffer_a = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://www.xiachufang.com/')
c.setopt(c.WRITEDATA, buffer_a)
c.perform()
c.close()

body = buffer_a.getvalue()
text = body.decode('utf-8')
print(text)

img_list = re.findall(r'src=\"(http://i5\.chuimg\.com/\w+\.jpg)', text)
# img_list = re.findall(r'src=\"\w+\.jpg', text) # this is wrong
pprint.pprint(img_list)


# create a folder
image_dir = os.path.join('/Users/markli/Downloads', 'images')
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

for img in img_list:
    o = urlparse(img)
    if '/' in o.path[1:]:
        opath = o.path[1:].replace('/', '_')
    else:
        opath = o.path[1:]
    filepath = os.path.join(image_dir, opath)
    with open(filepath, 'wb') as f:
        c = pycurl.Curl()
        c.setopt(c.URL, img)
        c.setopt(c.WRITEDATA, f)
        c.perform()
        c.close()
~~~

#### Use linux command to downlaod XIACHUFANG homepage pictures

~~~linux
curl http://www.xiachufang.com/ |grep -E 'src=\"(http://i5\.chuimg.com/\w+\.jpg)' |more 

curl http://www.xiachufang.com/ |grep -oP '(?<=src=\")http://i5\.chuimg.com/\w+\.jpg' |more    ?????好像有点问题

curl -s http://www.xiachufang.com/|grep -oP '(?<=src=\")http://i5\.chuimg\.com/\w+\.jpg'|xargs -i curl {} -O   ?????有问题

curl -s http://www.xiachufang.com/|grep -oP '(?<=src=\")http://i5\.chuimg\.com/\w+\.jpg' |xargs -i curl --create-dir {} -o ./images/{}    ????好像有点问题，这些命令应该是在linux系统下运行的， mac terminal运行可能会有问题

~~~








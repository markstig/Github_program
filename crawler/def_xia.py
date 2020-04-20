import requests
from bs4 import BeautifulSoup
import lxml
import os

def getpics(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    print('The status code is: ', r.status_code)
    print('The reason code is: ', r.reason)
    soup = BeautifulSoup(r.content, 'lxml')
    imgs = soup.select('img')
    collection = []
    for i in imgs:
        if 'data-src' in i.attrs:
            a = (i.attrs['alt'].replace('/', '_'), i.attrs['data-src'].split('@')[0])
            collection.append(a)
        else:
            a = (i.attrs['alt'].replace('/', '_'), i.attrs['src'].split('@')[0])
            collection.append(a)
    downloadpath = '/users/markli/downloads/'
    os.chdir(downloadpath)
    for k, v in collection:
        with open('%s.jpg'%k, 'wb') as f:
            for chunk in requests.get(v).iter_content(1024):
                f.write(chunk)
            f.close()
        size = os.path.getsize(downloadpath + '%s.jpg'%k)
        print('%s.jpg'%k, ' has been downlaoded!', '>>>>', 'The size of the file is: ', size/1024/2014, 'Mb')
print(getpics('https://www.xiachufang.com'))
import bs4, requests

def getcontent(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    selector = '.tb-detail-hd > h1'

    elems = soup.select(selector)
    return elems[0].text.strip()

ID = 'https://detail.tmall.com/item.htm?spm=a1z10.1-b-s.w5003-21795462378.3.529772d6K6dh9q&id=544842803277&scene=taobao_shop'

content = getcontent(ID)
print('The content is ' + content)



#Still couldn't get the tmall price 

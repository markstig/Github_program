spam = 'mma emby ella eva'

def findx(spam, x):
    n = 0
    for i in range(x):
        position = spam.find('e')
        n += position
        spam = spam[spam.find('e')+1:]
    return n

print(findx(spam, 2))
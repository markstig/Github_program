# Python Requests Tutorial: Request Web Pages, Download Images, POST Data, Read JSON, and More
# https://www.youtube.com/watch?v=tb8gHvYlCFs

import requests, pprint

# *Normal get conent
r = requests.get('https://xkcd.com/500/')

print(r)
print(r.status_code)  # 200 is running OK
print(r.ok)  # if less than 400, it will return True

# pprint.pprint(dir(r))

# pprint.pprint(help(r))

pprint.pprint(r.text)


# *Download a picture
r = requests.get('https://imgs.xkcd.com/comics/election.png')
# print(r.content)
# print(r.headers)
with open('comic.png', 'wb') as f:
    f.write(r.content)

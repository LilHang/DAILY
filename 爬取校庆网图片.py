import requests
import os
from bs4 import BeautifulSoup

url = 'http://70.neau.edu.cn/info/9989/85991.htm'
html = requests.get(url).text

soup = BeautifulSoup(html, features='lxml')
img_tr = soup.find_all('tr')

os.makedirs('D:\\code\\img_test', exist_ok=True)

for tr in img_tr:
    imgs = tr.find_all('img')
    for img in imgs:
        img_url = img['src']
        r = requests.get(img_url, stream=True)
        img_name = img_url.split('/')[-1]
        with open('D:\\code\\img_test\\%s' % img_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=256):
                f.write(chunk)

        # from urllib.request import urlretrieve
        # urlretrieve(img_url, 'D:\\code\\img_test\\%s' % img_name)

        # r = requests.get(img_url)
        # with open('D:\\code\\img_test\\%s' % img_name, 'wb') as f:
        #     f.write(r.content)

        print('Saved as %s' % img_name)









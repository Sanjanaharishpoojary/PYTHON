import requests,os
from bs4 import BeautifulSoup as BS
folder=input("enter the directory")

if not os.path.isdir(folder):
    os.makedirs(folder)

for i in range(2818,-1,-1):
    url=f'https://xkcd.com/{i}'
    img_url=BS(requests.get(url).content,'html.parser').find(id='comic').img['src']
    open(f'{folder}/image{i}.png','wb').write(requests.get(f'https:{img_url}').content)
    print(f'downloading:https:{img_url}')
#抓取 小雞上工 任務的html
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import collections #debug
collections.Callable = collections.abc.Callable
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.chickpt.com.tw/cases'
mission = input('要找什麼工作? 請輸入:')
count = input('要找幾頁? 請輸入:')
time = 1
#print(type(url))

for page in range(int(count)):
    print('\n第',time,'頁:')
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    for tag in tags:
        cla = tag.get('title', None)
        if cla!= None:
            if (mission in cla) == True:
                print('任務: ',cla)
                       
    
    time += 1
    url = 'https://www.chickpt.com.tw/cases?page='+str(time)
    #print(url)
    
from bs4 import BeautifulSoup
import re

d = {'icon-yz' : '1',
'icon-wx' : '2',
'icon-vu' : '3',
'icon-ts' : '4',
'icon-rq' : '5',
'icon-po' : '6',
'icon-nm' : '7',
'icon-lk' : '8',
'icon-ji' : '9',
'icon-acb' : '0',
'icon-dc' :'+',
'icon-fe' :'(' ,
'icon-hg' :')' ,
'icon-ba' :'-' }

def number_extract(score):
    # print(score)
    str1 = ''
    soup = BeautifulSoup(score, "html.parser")
    for s in soup.findAll("span"):
        s=str(s)
        temp = re.search(r'(?=icon-)[^"]*',s).group()
        str1 += d[temp]
    # print(str1[7:])
    return str1[7:]
# print(str1[6:])
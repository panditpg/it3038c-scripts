from bs4 import BeautifulSoup
import requests, re

r = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/phones').content
soup = BeautifulSoup(r, "lxml")

##tags = soup.findAll("a", {"href":re.compile('(allinone)')})
tags = soup.findAll("div", {"class":re.compile('(ratings)')})
##for a in tags:
for p in tags:
    w = p.findAll("p",{"class":"pull-right"})
    ##print(type(w))
    print(w[0].string)
    ##print(a.get('href'))



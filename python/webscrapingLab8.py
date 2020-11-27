from bs4 import BeautifulSoup
import requests, re

###r = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/phones').content
r = requests.get('https://en.wikipedia.org/wiki/Web_scraping').content
###soup = BeautifulSoup(r, "lxml")
if r.status_code == 200:
	soup: bs4.BeautifulSoup = BeautifulSoup(r.content, "html.parser")
    
    for headline in soup.find_all("span", {"class": "mw-headline"})
        print(headline.text)

##tags = soup.findAll("a", {"href":re.compile('(allinone)')})
###tags = soup.findAll("a", {"class":re.compile('(title)')})
##for a in tags:
###print(tags)
###for h in tags:
    ##w = p.findAll("p",{"class":"pull-right"})
    ##print(type(w))
    ###print(h[0].string)
    ##print(a.get('href'))
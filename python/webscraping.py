from bs4 import BeautifulSoup
import requests, re

r = requests.get('https://analytics.usa.gov').content
soup = BeautifulSoup(r, "lxml")
print('soup type')
print(type(soup))
print('soup output')
##print(soup.prettify())

for link in soup.find_all('a', attrs={'href':re.compile("^https://github.com")}):
     print(link.get('href'))
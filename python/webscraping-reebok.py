from bs4 import BeautifulSoup
import requests, re

r = requests.get('https://www.reebok.com/us/flexagon-energy-shoes---preschool/DV8354.html').content
soup = BeautifulSoup(r, 'html.parser')
print(soup)
##span = soup.find("h1", {"class":"product_information_title___2rG9M product_title gl-heading gl-heading--m"})
span = soup.find("h1", {"class":"gl-heading gl-heading--regular gl-heading--italic name__1Es"})
title = span.text
##span = soup.find("span", {"class":"gl-price__value gl-price__value--sale"})
##title = span.text

print("Item name: %s" % (title))
##print("Item %s has price %s" % (title, price))

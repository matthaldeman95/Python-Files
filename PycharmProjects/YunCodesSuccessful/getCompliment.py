#!/usr/bin/python
import BeautifulSoup
import newurllib2
import time
Soup = BeautifulSoup.BeautifulSoup
response = newurllib2.urlopen('http://emergencycompliment.com/')
time.sleep(1)
soup = Soup(response.read())

#print soup.prettify()

#print(soup.find("div", attrs={"class": "seven columns centered"}).contents)
print(soup.find("p", attrs={"class": "compliment"}).contents)
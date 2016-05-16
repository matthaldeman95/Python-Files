#!/usr/bin/python
import BeautifulSoup
import newurllib2
Soup = BeautifulSoup.BeautifulSoup
response = newurllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?id=4809537&mode=xml&APPID=bbd9de04c7a74e6cbaaf0a144e69e167&units=imperial').read()
soup = Soup(response)
#print soup.prettify()

print soup.find('weather')['number']
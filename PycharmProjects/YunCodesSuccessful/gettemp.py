#!/usr/bin/python
import BeautifulSoup
import newurllib2
Soup = BeautifulSoup.BeautifulSoup
response = newurllib2.urlopen('http://weather.yahooapis.com/forecastrss?w=2425834').read()
soup = Soup(response)
temp = (soup.find("yweather:condition")['temp'])
datastring = "Temperature: %s" % (temp)
print datastring


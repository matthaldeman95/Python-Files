#!/usr/bin/python
import BeautifulSoup
import newurllib2
Soup = BeautifulSoup.BeautifulSoup
response = newurllib2.urlopen('http://weather.yahooapis.com/forecastrss?w=2425834').read()
soup = Soup(response)

forecasts = soup.findAll('yweather:forecast')

fc = Soup(str(forecasts[0]))
day = fc.find("yweather:forecast")['day']
text = fc.find("yweather:forecast")['text']
low = fc.find("yweather:forecast")['low']
high = fc.find("yweather:forecast")['high']
print("Today (%s) : %s, %s-%s" % (day, text, low, high))

fc = Soup(str(forecasts[1]))
day = fc.find("yweather:forecast")['day']
text = fc.find("yweather:forecast")['text']
low = fc.find("yweather:forecast")['low']
high = fc.find("yweather:forecast")['high']
print("Tomorrow (%s) : %s, %s-%s" % (day, text, low, high))
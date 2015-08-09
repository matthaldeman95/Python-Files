

import urllib2
import BeautifulSoup

Soup = BeautifulSoup.BeautifulSoup

response = urllib2.urlopen('http://weather.yahooapis.com/forecastrss?w=2425834').read()
soup = Soup(response)
print(soup.prettify())

print('Current condition:'),
print(soup.find("yweather:condition")['text'])
print('Temperature: '),
print(soup.find("yweather:condition")['temp'])

forecasts = soup.findAll('yweather:forecast')
today = Soup(str(forecasts[0]))
tomorrow = Soup(str(forecasts[1]))

print("Today ("),
print(today.find("yweather:forecast")['day']),
print(") : "),
print(today.find("yweather:forecast")['text']),
print(","),
print(today.find("yweather:forecast")['low']),
print("-"),
print(today.find("yweather:forecast")['high'])

print("Tomorrow ("),
print(tomorrow.find("yweather:forecast")['day']),
print(") : "),
print(tomorrow.find("yweather:forecast")['text']),
print(","),
print(tomorrow.find("yweather:forecast")['low']),
print("-"),
print(tomorrow.find("yweather:forecast")['high'])
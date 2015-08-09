import urllib2
import BeautifulSoup

Soup = BeautifulSoup.BeautifulSoup

response = urllib2.urlopen('http://www.dcunited.com/standings').read()
soup = Soup(response)
print(soup.prettify())

divs = (soup.findAll("D.C. United"))
print(divs)

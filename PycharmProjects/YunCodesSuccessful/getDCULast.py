#!/usr/bin/python
import BeautifulSoup
import newurllib2
Soup = BeautifulSoup.BeautifulSoup
response = newurllib2.urlopen('http://www.dcunited.com/').read()
soup = Soup(response)

#print(soup.prettify())
lastmatch = soup.find("span", attrs={"class": "match_summary"}).contents
laststr = str(lastmatch)
foo, last, bar = laststr.split("'")
print("DCU Last Match: "),
print(last)

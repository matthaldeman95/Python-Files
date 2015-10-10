#!/usr/bin/python
import BeautifulSoup
import newurllib2
Soup = BeautifulSoup.BeautifulSoup
response = newurllib2.urlopen('http://www.dcunited.com/').read()
soup = Soup(response)
print(soup.prettify())

nextmatch = soup.find("span", attrs={"class": "match_summary "}).contents
nextstr = str(nextmatch)
foo, next, bar = nextstr.split("'")
day, date, year = next.split(",")
nextvs = soup.find("span", attrs={"class": "match_summary versus"}).contents
vsstr = str(nextvs)
foo, vs, bar = vsstr.split("'")
timeloc = soup.find("div", attrs={"class": "match_info"}).contents
timestr = str(timeloc)
foo, time, bar = timestr.split('"')
short = time[:6]
print("DCU Next Match: %s,%s %s%s" % (day, date, vs, short))



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
nextvs = soup.find("span", attrs={"class": "match_summary versus"}).contents
vsstr = str(nextvs)
foo, vs, bar = vsstr.split("'")
timeloc = str(soup.find("div", attrs={"class": "match_info"}).contents)
print timeloc

#foo, time, bar = timestr.split('"')
#print("DCU Next Match: %s %s %s" % (next, vs, time))



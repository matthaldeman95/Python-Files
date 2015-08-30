#!/usr/bin/python
import BeautifulSoup
import newurllib2
Soup = BeautifulSoup.BeautifulSoup
response = newurllib2.urlopen('http://www.dcunited.com/').read()
soup = Soup(response)

nextmatch = soup.find("span", attrs={"class": "match_summary "}).contents
nextstr = str(nextmatch)
foo, next, bar = nextstr.split("'")
nextvs = soup.find("span", attrs={"class": "match_summary versus"}).contents
vsstr = str(nextvs)
foo, vs, bar = vsstr.split("'")
nextinfo = soup.find("div", attrs={"class": "match_info"}).contents
infostr = str(nextinfo)
foo, info, bar = infostr.split("'")
print("Next Match: "),
print(next),
print(vs),
print(info)
#!/usr/bin/python
import BeautifulSoup
import newurllib2
Soup = BeautifulSoup.BeautifulSoup
response = newurllib2.urlopen('http://www.dcunited.com/standings').read()
soup = Soup(response)
#print soup.prettify()

dcrow = soup.find("tr", attrs={"class": "hub_club even"})
print dcrow.prettify()

rank = str(dcrow.find("td", attrs={"class": "hide-column"}).contents)
foo, rank, bar = rank.split("'")
gp = str(dcrow.find("td", attrs={"data-title": "Games Played"}).contents)
foo, gp, bar = gp.split("'")
w = str(dcrow.find("td", attrs={"data-title": "Wins"}).contents)
foo, w, bar = w.split("'")
l = str(dcrow.find("td", attrs={"data-title": "Losses"}).contents)
foo, l, bar = l.split("'")
t = str(dcrow.find("td", attrs={"data-title": "Ties"}).contents)
foo, t, bar = t.split("'")


print("DCU (%s): %s/%s/%s" % (rank, w, l,t))




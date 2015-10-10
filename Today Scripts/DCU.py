#!/usr/bin/python
import BeautifulSoup
import newurllib2
Soup = BeautifulSoup.BeautifulSoup
response = newurllib2.urlopen('http://www.dcunited.com/standings').read()
soup = Soup(response)

if soup.find("tr", attrs={"class": "hub_club even"}):
    dcrow = soup.find("tr", attrs={"class": "hub_club even"})
elif soup.find("tr", attrs={"class": "hub_club odd"}):
    dcrow = soup.find("tr", attrs={"class": "hub_club odd"})

rank = str(dcrow.find("td", attrs={"data-title": "Rank"}).contents)
foo, rank, bar = rank.split("'")
gp = str(dcrow.find("td", attrs={"data-title": "Games Played"}).contents)
foo, gp, bar = gp.split("'")
w = str(dcrow.find("td", attrs={"data-title": "Wins"}).contents)
foo, w, bar = w.split("'")
l = str(dcrow.find("td", attrs={"data-title": "Losses"}).contents)
foo, l, bar = l.split("'")
t = str(dcrow.find("td", attrs={"data-title": "Ties"}).contents)
foo, t, bar = t.split("'")

response = newurllib2.urlopen('http://www.dcunited.com/schedule').read()
soup = Soup(response)


games = soup.findAll("article", attrs={"class": "match_item featured twoclub"})
soup = Soup(str(games[1]))
#print soup.prettify()
date = str(soup.find("div", attrs={"class": "match_details upcoming"}).contents)
foo, date, bar = date.split("'")
#print date
timesoup = Soup(str(soup.find("div", attrs={"class": "timing"}).contents))
time = str(timesoup.find("div", attrs={"class": "match_info"}).contents)
foo, time, bar = time.split("'")
#print time



print("Rank: %s, Record: %s/%s/%s" % (rank, w, l, t))
print("Next match: %s %s" % (date, time))
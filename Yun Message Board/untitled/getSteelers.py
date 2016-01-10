__author__ = 'Matt'
#!/usr/bin/python
import BeautifulSoup
import newurllib2
import datetime
Soup = BeautifulSoup.BeautifulSoup
response = newurllib2.urlopen('http://www.nfl.com/teams/pittsburghsteelers/schedule?team=PIT').read()
soup = Soup(response)

ranking = str(soup.find("p", attrs={"class": "team-overall-ranking"}).contents)


foo, rank, record = ranking.split("'")
rank = rank.strip()
foo, rec, bar = record.split("<")
foo, newrec = rec.split(">")
foo, newrec = newrec.split("(")
newrec, bar = newrec.split(")")


response = newurllib2.urlopen('http://www.sbnation.com/nfl/teams/pittsburgh-steelers').read()
soup = Soup(response)
soup = Soup(str(soup.find("div", attrs={"class": "sbn-pte-head-team-next-game"}).contents))
next = str(soup.find("p").contents)
foo, date, bar = next.split("        ")
date = date.strip()
date, bar = date.split("EST")
day, date, year, time = date.split(",")
day = day.strip()
date = date.strip()
m, d = date.split(" ")
d = int(d)

print("Steelers (%s, %s) Next Game: %s, %s,%s" % (rank, newrec, day, date, time))
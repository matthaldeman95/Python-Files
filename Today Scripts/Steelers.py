#!/usr/bin/python
import BeautifulSoup
import newurllib2
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
date, bar = date.split("EDT")

print("Rank: %s, Record: %s" % (rank, newrec))
print("Next game: %s" % (date))


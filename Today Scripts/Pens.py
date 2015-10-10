#!/usr/bin/python
import BeautifulSoup
import newurllib2
Soup = BeautifulSoup.BeautifulSoup
response = newurllib2.urlopen('http://www.cbssports.com/nhl/teams/page/PIT/pittsburgh-penguins').read()
soup = Soup(response)


rec = str(soup.find("div", attrs={"class": "record"}).contents)
url, rec, other = rec.split(">")
rec, other = rec.split("|")
rec = rec.strip()
rec, bar = rec.split(" ")


foo, rank = other.split("Metropolitan")
rank, bar = rank.split("<")
rank = rank.strip()
foo, rank = rank.split("(")
rank, bar = rank.split(")")
rank, bar = rank.split("t")

soup = Soup(str(soup.find("div", attrs={"class": "matchUpTeams"}).contents))


dt = str(soup.find("div").contents)
foo, date, other = dt.split("'")


foo, other, bar = other.split(">")
time, bar = other.split("<")

print("Rank: %s, Record: %s" % (rank, rec))
print("Next game: %s%s" % (date, time))



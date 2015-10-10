#!/usr/bin/python
import BeautifulSoup
import newurllib2
Soup = BeautifulSoup.BeautifulSoup
response = newurllib2.urlopen('http://www.nfl.com/teams/pittsburghsteelers/schedule?team=PIT').read()
soup = Soup(response)

ranking = str(soup.find("p", attrs={"class": "team-overall-ranking"}).contents)

foo, rank, record = ranking.split("'")
foo, rec, bar = record.split("<")
foo, newrec = rec.split(">")

newsoup = Soup(str(soup.find("div", attrs={"class": "schedules-list-hd pre"})))

date = str(soup.find("span", attrs={"class": "date"}).contents)
foo, date, bar = date.split("'")
time = str(soup.find("span", attrs={"class": "time"}).contents)
foo, time, bar = time.split("'")
et = str(soup.find("span", attrs={"class": "et"}).contents)
foo, et, bar = et.split("'")

if soup.find("span", attrs={"class": "at "}):
        loc = str(soup.find("span", attrs={"class": "at "}).contents)
        foo, loc, bar = loc.split("'")
elif soup.find("span", attrs={"class": "at hide"}):
        loc = "vs"

if soup.find("span", attrs={"class": "team-name home "}):
        opp = str(soup.find("span", attrs={"class": "team-name home "}).contents)
        foo, opp, bar = opp.split("'")
elif soup.find("span", attrs={"class": "team-name away "}):
        opp = str(soup.find("span", attrs={"class": "team-name away "}).contents)
        foo, opp, bar = opp.split("'")

print("PBS: %s%s Next: %s %s%s %s %s" %  (rank, newrec, date, time, et, loc, opp))



#!/usr/bin/python
import BeautifulSoup
import newurllib2
Soup = BeautifulSoup.BeautifulSoup
response = newurllib2.urlopen('http://www.dcunited.com/').read()
soup = Soup(response)

dateline = soup.find("span", attrs={"class": "date"}).contents
datestr = str(dateline)
foo, date, bar = datestr.split("'")
day, year = date.split(",")
teamline = soup.find("div", attrs={"class": "away-team"}).contents
teamstr = str(teamline)
foo, team, bar = teamstr.split("'")
timeline = soup.find("span", attrs={"class": "time"}).contents
timestr = str(timeline)
foo, time, bar = timestr.split("'")
print("DCU next match: %s %s %s" % (day, time, team))
#!/usr/bin/python
import BeautifulSoup
import newurllib2
import re
import datetime
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



soup = Soup(str(soup.find("div", attrs={"class": "matchUpTeams"}).contents))



dt = str(soup.find("div").contents)
foo, date, other = dt.split("'")
day, date, bar = date.split(",")

if re.search(day, 'Mon'):
    day = "Monday"
elif re.search(day, 'Tue'):
    day = "Tuesday"
elif re.search(day, 'Wed'):
    day = "Wednesday"
elif re.search(day, 'Thu'):
    day = "Thursday"
elif re.search(day, 'Fri'):
    day = "Friday"
elif re.search(day, 'Sat'):
    day = "Saturday"
elif re.search(day, 'Sun'):
    day = "Sunday"

date = date.strip()
if re.search(date, '  '):
    m, d = date.split("  ")
else:
    m, d = date.split(" ")
m = m.strip();
d = d.strip()
d = int(d)


if(m == "January"):
    m = "Jan"
elif(m == "February"):
    m = "Feb"
elif(m == "March"):
    m = "Mar"
elif(m == "April"):
    m = "Apr"
elif(m == "September"):
    m = "Sept"
elif(m == "October"):
    m = "Oct"
elif(m == "November"):
    m = "Nov"
elif(m == "December"):
    m = "Dec"



foo, other, bar = other.split(">")
time, bar = other.split("<")
time, pm, zone = time.split(" ")

today = datetime.date.today()
today = today.day


print("Rank: %s Metro Div, Record: %s" % (rank, rec))
print(" ")
if(d == today):
    print("Next game:  Today, %s %s" % (time, pm))
else:
    print("Next game:  %s, %s %s, %s %s"% (day, m, d, time, pm))



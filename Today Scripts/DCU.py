#!/usr/bin/python
import BeautifulSoup
import newurllib2
import datetime
Soup = BeautifulSoup.BeautifulSoup
response = newurllib2.urlopen('http://www.dcunited.com/standings').read()
soup = Soup(response)
month = ["blah", "Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

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
day, date = date.split(" ")
day = day.strip();
if(day == "SUN"):
    day = "Sunday"
elif(day == "MON"):
    day = "Monday"
elif(day == "TUE"):
    day = "Tuesday"
elif(day == "WED"):
    day = "Wednesday"
elif(day == "THU"):
    day = "Thursday"
elif(day == "FRI"):
    day = "Friday"
elif(day == "SAT"):
    day = "Saturday"
m, d, y = date.split("/")
m = int(m)
m = month[m]
d = int(d)


timesoup = Soup(str(soup.find("div", attrs={"class": "timing"}).contents))
time = str(timesoup.find("div", attrs={"class": "match_info"}).contents)
foo, time, bar = time.split("'")
time, zone = time.split(" ")
time, bar = time.split("PM")

today = datetime.date.today()
today = today.day

print("Rank: %s East, Record: %s-%s-%s" % (rank, w, l, t))
print(" ")
if d == today:
    print("Next match:  Today, %s PM" % (time))
else:
    print("Next match: %s, %s %s, %s PM" % (day, m, d, time))

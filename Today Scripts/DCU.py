#!/usr/bin/python
import BeautifulSoup
import newurllib2
import datetime
Soup = BeautifulSoup.BeautifulSoup

response = newurllib2.urlopen('http://www.dcunited.com/standings').read()
soup = Soup(response)
classes = Soup(str(soup.findAll('tr')))

for c in classes:
    c = Soup(str(c))
    #print c.prettify()
    data = c.find("td", attrs={"data-title": "Club"})
    if data:
        data = data.contents
        foo, data, bar = str(data).split("'")
        if data=="D.C. United":
            break
        else: continue

rank = str(c.find("td", attrs={"data-title": "Rank"}).contents)
foo, rank, bar = rank.split("'")
record = str(c.find("td", attrs={"data-title": "W-L-T"}).contents)
foo, record, bar = record.split("'")
"""
month = ["blah", "Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]


response = newurllib2.urlopen('http://www.dcunited.com/schedule').read()
soup = Soup(response)

print soup

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
"""
print("Rank: %s East, Record: %s" % (rank, record))
print(" ")
"""
if d == today:
    print("Next match:  Today, %s PM" % (time))
else:
    print("Next match: %s, %s %s, %s PM" % (day, m, d, time))
"""
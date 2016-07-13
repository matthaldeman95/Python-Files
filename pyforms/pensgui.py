#!/usr/bin/python
import BeautifulSoup
import newurllib2
import re

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
















date = date.strip()
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

print("Pens (%s, %s) Next Game: %s, %s %s, %s %s" % (rank, rec, day, m, d, time, pm))



outfile = open('/home/matthew/Desktop/html.html','w')
outfile.write('<!DOCTYPE html>'
              '<html>'
              '<body>'
              '<image src="logo.png></img>"'
              '<h1>Pittsburgh Penguins</h1>'
              )
outfile.write('<h2>Rank: %s Metro Div, Record: %s</h2>' % (rank,rec))
outfile.write('<h3>Next Game: %s, %s %s, %s %s</h3>' % (day,m,d,time,pm))
outfile.write('</body>'
              '</head>'
              )

outfile.close()
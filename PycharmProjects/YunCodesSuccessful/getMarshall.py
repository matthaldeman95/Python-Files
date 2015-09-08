#!/usr/bin/python
import BeautifulSoup
import newurllib2
Soup = BeautifulSoup.BeautifulSoup
response = newurllib2.urlopen('http://www.herdzone.com/sports/m-footbl/sched/mars-m-footbl-sched.html').read()
soup = Soup(response)

#print soup

new = Soup(str(soup.find("div", attrs={"id": "sched_records"}).contents))
#print new
record = str(new.find("div").contents)

foo, foo1, foo2, record, foo3 = record.split("'")
foo, record, foo1 = record.split("n")
record, foo = record.split(" ")


#print("Marshall Football (%s)" % (record))

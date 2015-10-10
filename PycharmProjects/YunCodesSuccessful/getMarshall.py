#!/usr/bin/python
import BeautifulSoup
import newurllib2
Soup = BeautifulSoup.BeautifulSoup
response = newurllib2.urlopen('http://www.herdzone.com/sports/m-footbl/sched/mars-m-footbl-sched.html').read()
soup = Soup(response)

print soup.prettify()


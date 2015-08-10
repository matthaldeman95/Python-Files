#!/usr/bin/python

from WeatherParse import temperature, condition, forecast
from DCUParse import nextgame
import sys

sys.path.insert(0, '/usr/lib/python2.7/bridge')

#bridgeclient is current problem, claims to be installed on Yun?
#from bridgeclient import BridgeClient as bridgeclient

temp = temperature()
print temp

cond = condition()
print cond

todayfc = forecast(0)
print todayfc

tomfc = forecast(1)
print tomfc

nextgame = nextgame()
print nextgame


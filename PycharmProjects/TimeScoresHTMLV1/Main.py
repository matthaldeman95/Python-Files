
from WeatherParse import temperature, condition, forecast
from DCUParse import nextgame

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


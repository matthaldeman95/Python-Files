def temperature():
    import newurllib2
    import BeautifulSoup
    Soup = BeautifulSoup.BeautifulSoup
    response = newurllib2.urlopen('http://weather.yahooapis.com/forecastrss?w=2425834').read()
    soup = Soup(response)
    return(soup.find("yweather:condition")['temp'])

def condition():
    import newurllib2
    import BeautifulSoup
    Soup = BeautifulSoup.BeautifulSoup
    response = newurllib2.urlopen('http://weather.yahooapis.com/forecastrss?w=2425834').read()
    soup = Soup(response)
    return(soup.find("yweather:condition")['text'])

def forecast(n):
    import newurllib2
    import BeautifulSoup
    Soup = BeautifulSoup.BeautifulSoup
    response = newurllib2.urlopen('http://weather.yahooapis.com/forecastrss?w=2425834').read()
    soup = Soup(response)
    forecasts = soup.findAll('yweather:forecast')
    fc = Soup(str(forecasts[n]))
    day = fc.find("yweather:forecast")['day']
    text = fc.find("yweather:forecast")['text']
    low = fc.find("yweather:forecast")['low']
    high = fc.find("yweather:forecast")['high']

    return("Today (%s) : %s, %s-%s" % (day, text, low, high))
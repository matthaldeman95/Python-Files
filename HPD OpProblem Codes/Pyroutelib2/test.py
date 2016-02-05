import loadOsm
import route
import routeAsCSV
import routeAsGpx
import tiledata
import tilenames
import weights



lat1 = 38.4205805
lon1 = -82.4267039
lat2 = 38.4144
lon2 = -82.4450
transport = 'car'

routeAsGpx [lat1] [lon1] [lat2] [lon2] [transport]
PYROUTELIB2

The Pyroutelib2 package is working fine for me.  I've been using the routeAsGpx.py command from the terminal.  Just cd into whatever folder it is in, then use:

                    routeAsGpx.py latitude1 longitude 1 latitude 2 longitude 2 car

Arguments are start and end coordinates, and mode of transportation.  Substitute in numbers for the coordinates but just type car for the 5th arg.

There's a bunch of package dependencies.  Follow the "import" statements at the top of all the individual files, and install everything you can.  If you don't know how to do this or need help, let me know.

Looking at the top of the routeAsGpx.py file, you'll need to change the "outfile" destination to somewhere on your computer.

Then if everything works correctly, you'll get a gpx file output at the location you specified which can then be opened into QGIS.


DIJKSTRA



The V1.py code in the Dijkstra algorithm folder is not working yet.  The code will run successfully, but will produce no results because I've commented out the lines that cause problems.  It's something wrong with the smopy package, which I need to figure out.  I should have it working in the next few days easily enough.

Again, lots of packages to install here

Here's the URL to where I found this code, which gives some good information about it and its dependencies

                                http://ipython-books.github.io/featured-03/






**I use the Mac terminal to do pretty much everything (installing packages, running codes, etc).

I honestly don't really know how to do it on a Windows.

We could all meet up sometime this week and go over Python stuff if anyone wants to.**

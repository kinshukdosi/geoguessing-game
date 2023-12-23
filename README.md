# geoguessing-game
Geography based guessing game using google maps API and python Flask

The aim is to guess the compass bearing when shown a street view image from google maps

To use:
add your own google maps API key to the 'key' variable on line 40 of views.py <br>
install python library flask via pip <br>

Currently, the places shown are based in Cheltenham, UK. <br>
These can be changed by retrieving coordinates and bearings from google maps and adding them to the 'dict' variable in views.py in the same format

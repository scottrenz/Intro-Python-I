# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class MyParentClass():
    def __init__(self, x, y):
        return x
class SubClass(MyParentClass):
    def __init__(self, x, y):
        super().__init__(x, y)
class LatLon():
    def c(self,lat,lon):
        return {'lat': lat,'lon': lon}
x = LatLon        
x = x.c(x,1,2)
print(x)
waypoint = 1
geocache = 2        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
class Waypoint(LatLon):
    super().__init__(name)
    x = LatLon.name=name
    return x
# YOUR CODE HERE

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE

# Print it--also make this print more nicely
print(geocache)

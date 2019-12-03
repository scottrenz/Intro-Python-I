# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def c(self):
        return {"lat": self.lat, "lon": self.lon}
x = LatLon.c(LatLon(1,2))
print(x)        
geocache = 2        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.
class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat,lon)
        self.name = name
    def c(self):
        return {"name": self.name, "lat": self.lat, "lon": self.lon}
waypoint = Waypoint.c(Waypoint("Way",1,2))
# YOUR CODE HERE

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size
    def c(self):
        return {"name": self.name, "difficulty": self.difficulty, "size": self.size, "lat": self.lat, "lon": self.lon}
geocache = Geocache.c(Geocache("Way","hard","large",1,2))

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521
waypoint = Waypoint.c(Waypoint("Catacombs", 41.70505, -121.51521))

# YOUR CODE HERE

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache.c(Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556))

# Print it--also make this print more nicely
print(geocache)

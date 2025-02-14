from classes.trip import Trip


class Visitor:

    all = []

    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)

    @property 
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) is str:
            if 1 <= len(name) <= 15:
                self._name = name
            else:
                raise ValueError("Name must be between 1 and 15 characters.")
        else:
            raise TypeError("Name must be a string.") 

    def trips(self):
        return [ trip for trip in Trip.all if trip.visitor is self]

    def national_parks(self):
        return list( set ( trip.national_park for trip in self.trips ()))

from classes.national_park import NationalPark
from classes.trip import Trip
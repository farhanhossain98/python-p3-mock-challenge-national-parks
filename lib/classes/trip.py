
class Trip:
    
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        if type(start_date) is str:
            self.start_date = start_date
        else: 
            raise TypeError("Start Date must be a string.")
        if type(end_date) is str:
            self.end_date = end_date
        else: 
            raise TypeError('End date must be a string.')
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, name):
        if type(name) is Visitor:
            self._visitor = name
        else:
            raise TypeError('Visitor must be an instance of the Visitor class')
    
    @property 
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, name):
        if type(name) is NationalPark:
            self._national_park = name
        else:
            raise TypeError('National park must be an instance of the NationalPark class.')


    

from classes.national_park import NationalPark
from classes.visitor import Visitor
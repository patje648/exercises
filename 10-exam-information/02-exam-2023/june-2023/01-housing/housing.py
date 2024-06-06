# enter your code here to solve the housing assignment
# voer hier je code in om de huisvestingsvraag op te lossen
from abc import ABC, abstractmethod
import re

from networkx import number_of_nodes


class Person:
    def __init__(self, id, name, is_a_student):
        if self.is_valid_name(name)==False:
            raise ValueError
        self.id=id
        self.name=name
        self.is_a_student=is_a_student

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name=name

    @staticmethod
    def is_valid_name(name):
        if re.match("[A-Za-z]+( [A-Za-z]+)+",name):
            return True
        return False

class Residence(ABC):
    def __init__(self, address, area, number_of_rooms):
        self.adress=address
        self.area=area
        self.number_of_rooms=number_of_rooms

        self.__occupants=dict()

    @property
    def number_of_occupants(self):
        return len(self.__occupants)
    @property
    def maximum_occupants(self):
        return min(self.area//20,self.number_of_occupants*2)

    def register_resident(self, person):
        if person.id not in self.__occupants:
            self.__occupants[person.id] = person
        if self.number_of_occupants == self.maximum_occupants:
            raise RuntimeError
        
    def unregister_resident(self,id):
        self.occupants.pop(id)

    @property
    def resident_names(self):
        return [Person.name for person in self.__occupants.values()]
    
    @abstractmethod
    def calculate_value(self):
        ...

class Villa(Residence):
    def __init__(self,address,area,number_of_rooms,garage_capacity):
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity=garage_capacity

    

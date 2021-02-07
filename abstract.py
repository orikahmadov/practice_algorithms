from abc import abstractmethod, ABCMeta
"""In classic object-oriented terminology, we say a class is an abstract base class
if its only purpose is to serve as a base class through inheritance. More formally,
an abstract base class is one that cannot be directly instantiated, while a concrete
class is one that can be instantiated. By this definition, our Progression class is
technically concrete, although we essentially designed it as an abstract base class."""

class Sequence(metaclass=ABCMeta):
    """Our version of collections.Sequence abstract base class"""
    
    @abstractmethod
    def __len__(self):
        """returns length of the sequence"""

    @abstractmethod
    def __getitem__(self, i):
        """Returns an element at the i index of sequence """

    def __contains__(self, item):
        """returns True if the value is in the sequence otherwise False"""
        for i in range(len(self)):
            if self[i] == item:
                return True
        else:           #end of loop
            return False

    def index(self, val):
        for i in range(len(self)):
            if self[i] == val:
                return i
        else:
            raise ValueError("Value is not in the sequence")


    def count(self, val):
        """Counts how many times an item occurs in the list"""
        counter = 0
        for i in range(len(self)):
            if self[i] == val:
                counter += 1
            else:
                continue
        else:
            return counter



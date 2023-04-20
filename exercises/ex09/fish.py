"""File to define Fish class."""

__author__ = "740461000"


class Fish:
    """This is initiating a new class called Fish."""
    
    age: int 

    def __init__(self):
        """Initialize the age of Fish."""
        self.age = 0
        return None
    
    def one_day(self):
        """Increase the age attribute of fish by one each day."""
        self.age += 1
        return None
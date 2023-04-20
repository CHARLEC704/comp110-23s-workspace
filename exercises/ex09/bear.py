"""File to define Bear class."""

__author__ = "740461000"


class Bear:
    """This is initiating a new class called Bear."""

    age: int
    hunger_score: int

    def __init__(self):
        """Constructor to initialize age and hunger score attributes."""
        self.age = 0
        self.hunger_score = 0
        return None
    
    def one_day(self):
        """For each day, add a day and decrease the hunger score."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """For every fish eaten, increase the hunger score buy that amount."""
        self.hunger_score += num_fish
        return None
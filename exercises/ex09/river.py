"""File to define River class."""

__author__ = "740461000"

from exercises.ex09.fish import Fish
from exercises.ex09.bear import Bear


class River:
    """This is initiating a new class called River that would incorporate Fish and Bear classes."""

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears.."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check ages of fish and bears, if they are less than age limits, add them to new lists of survivors and then set that as new list."""
        fish_survivors: list[Fish] = list()
        bear_survivors: list[Bear] = list()
        for fish in self.fish:
            if fish.age <= 3:
                fish_survivors.append(fish)
        for bear in self.bears:
            if bear.age <= 5:
                bear_survivors.append(bear)
        self.fish = fish_survivors
        self.bears = bear_survivors
        return None
    
    def remove_fish(self, amount: int):
        """Given some abitrary amount, remove the fish at that number of indices."""
        if amount < len(self.fish):
            for fish in range(0, amount):
                self.fish.pop(0)
        else:
            self.fish = []
        return None

    def bears_eating(self):
        """This method connects other methods by initiatinng the removal function of a number of fish and the eating function for Bears."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
            else:
                bear.eat(0)
        return None
    
    def check_hunger(self):
        """This method removes starved bears from the list by generating a new list of survivor bears with non-negative hunger scores."""
        unstarved_bears: list[Bear] = list()
        for bear in self.bears:
            if bear.hunger_score >= 0:
                unstarved_bears.append(bear)
        self.bears = unstarved_bears
        return None
    
    def repopulate_fish(self):
        """This method increases the number of fish in the list by using an mathematical function to determine how many fish to add."""
        added_num: int = 4 * (len(self.fish) // 2)
        while added_num > 0:
            self.fish.append(Fish)
            added_num -= 1
        return None
    
    def repopulate_bears(self):
        """This method increases the number of bears in the list by using an mathematical function to determine how many bears to add."""
        added_num: int = len(self.bears) // 2
        while added_num > 0:
            self.bears.append(Bear)
            added_num -= 1
        return None
    
    def view_river(self):
        """This method notifies the games user the day and respective populations of fish and bears."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Call the River's one_river_day seven times."""
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        River.one_river_day(self)
        return None
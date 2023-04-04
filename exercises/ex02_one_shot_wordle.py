"""EX02 One Shot Wordle!"""
__author__ = "730461000"

SECRET: str = "python"
playing: bool = True
number_letters: str = str(len(SECRET))
guess: str = input("What is your " + number_letters + "-letter guess?")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index_guess: int = 0
resulting_emoji: str = ""


while len(guess) != len(SECRET):
    guess = str(input("That was not " + number_letters + "-letters! Try again:"))

while index_guess < len(SECRET):
    if guess[index_guess] == SECRET[index_guess]:
        resulting_emoji = resulting_emoji + GREEN_BOX
    else:
        missplaced_letter: bool = False
        alternate_indices: int = 0
        while missplaced_letter is False and alternate_indices < len(SECRET):
            if SECRET[alternate_indices] == guess[index_guess]:
                missplaced_letter = True
            alternate_indices = alternate_indices + 1
        if missplaced_letter is True:
            resulting_emoji = resulting_emoji + YELLOW_BOX
        else:
            resulting_emoji = resulting_emoji + WHITE_BOX
    index_guess = index_guess + 1
print(resulting_emoji)
if guess != SECRET:
    print("Not quite. Play again soon!")        
else: 
    print("Woo! You got it! ") 
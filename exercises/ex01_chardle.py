"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730461000"

first_word: str = input("Enter a 5-character word:")
if (len(first_word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
first_character: str = input("Enter a single character:")
if (len(first_character) != 1):
    print("Error: Character must be a single character.")
    exit()
num_matching_characters: int = 0
print("Searching for " + first_character + " in " + first_word)
if (first_word[0] == first_character):
    print(first_character + " found at index 0")
    num_matching_characters += 1
if (first_word[1] == first_character):
    print(first_character + " found at index 1")
    num_matching_characters += 1
if (first_word[2] == first_character):
    print(first_character + " found at index 2")
    num_matching_characters += 1
if (first_word[3] == first_character):
    print(first_character + " found at index 3")
    num_matching_characters += 1
if (first_word[4] == first_character):
    print(first_character + " found at index 4")
    num_matching_characters += 1
if (num_matching_characters > 1):
    print(str(num_matching_characters) + " instances of " + first_character + " found in " + first_word)
if (num_matching_characters == 0):
    print("No instances of " + first_character + " found in " + first_word)
if (num_matching_characters == 1):
    print(str(num_matching_characters) + " instance of " + first_character + " found in " + first_word)
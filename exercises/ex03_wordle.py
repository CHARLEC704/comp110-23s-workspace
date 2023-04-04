"""EX03 Wordle."""
__author__ = "730461000"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    # your code will go here
    num_turns: int = 1
    secret: str = "codes"
    while num_turns <= 6:
        print(f"===Turn {num_turns}/6===")
        guess_global: str = input_guess(len(secret))
        resulting_emojis: str = emojified(guess_global, secret)
        print(resulting_emojis)
        if guess_global == secret:
            print(f"You won in {num_turns}/6 turns!")
            return
        else:
            num_turns = num_turns + 1
    print("X/6 - Sorry, try again tomorrow!")
    

def contains_char(any_length_str: str, single_char: str) -> bool:
    """Searching for character at each index of string."""
    assert len(single_char) == 1
    idx_any_length: int = 0
    while idx_any_length < len(any_length_str):
        if single_char == any_length_str[idx_any_length]:
            return True
        else:
            idx_any_length = idx_any_length + 1 
    return False


def emojified(guess: str, secret: str) -> str:
    """Matching incorrect guess with white box, missplaced characters with yellow box, and correct with green."""
    assert len(guess) == len(secret)
    resulting_emoji: str = ""
    idx_guess: int = 0
    while idx_guess < len(secret):
        if guess[idx_guess] == secret[idx_guess]:
           resulting_emoji = resulting_emoji + GREEN_BOX
        else:
            if contains_char(secret, guess[idx_guess]) is True:
                resulting_emoji = resulting_emoji + YELLOW_BOX
            else:
                resulting_emoji = resulting_emoji + WHITE_BOX
        idx_guess = idx_guess + 1
    return resulting_emoji


def input_guess(guess_correct_len: int) -> str:
    """Prompt correct length of function to be inputed and return guess of correct length."""
    guess_correct: str = input(f"Enter a {guess_correct_len} character word: ")
    while len(guess_correct) != guess_correct_len:
        guess_correct = input(f"That wasn't {guess_correct_len} chars! Try again: ")
    return guess_correct


if __name__ == "__main__":
    main()
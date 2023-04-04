"""EX06 -- Choose Your Own Adventure -- Major Recommender."""

__author__ = "730461000"

#Disclaimer for grader: this game is not mean't to offend any particular major. As a student double majoring in one BA degree and one BS, there are great majors in each category.



player: str = ""
points: int = 0
major_recommendation: str = ""
game_loop: bool = True
MAP: str = "\U0001F30F"
HOSPITAL: str = "\U0001F3E5"
MAIL: str ="\U0001F4E8"
ABACUS: str = "\U0001F9EE"
NEWSPAPER: str = "\U0001F4F0"
CHART: str = "\U0001F4B9"
BOLT: str = "\U0001F529"
HELIX: str = "\U0001F9EC"
TUBE: str = "\U0001F9EA"
ARM: str = "\U0001F9BE"
SLEEP: str = "\U0001F4A4"
SPEAKER: str = "\U0001F4E2"
MAGNET: str = "\U0001F9F2"
RULER: str = "\U0001F4D0"
BRIEFCASE: str = "\U0001F4BC"
LAPTOP: str = "\U0001F4BB"


def main() -> None:
    """Entry point to the game where a player chooses 1 of three paths."""
    greet()
    global game_loop
    
    while game_loop == True:
        global major_recommendation
        major_overview: str = input("To pursue a Bachelor of Science, type 'BS'. To purse a Bachelor of Arts, type 'BA'. Otherwise, type 'end' to exit the quiz. If you are indecisive and want a random recomendation, type 'indecisive'. ")
        if major_overview == "end":
            print(f"A little overwhelming? No worries! You had {points} points so are {major_recommendation}. Check out some classes in different departments and try again another day.")
            game_loop = False
        else:
            if major_overview == "BS":
                bach_sci()
            if major_overview == "BA":
                bach_art()
            if major_overview == "indecisive":
                indec()
        major_recommendation = final_rec(points)
        if major_recommendation == "Undecided":
            print(f"You earned {points} and therefore, seem to be {major_recommendation}. Check out some classes in different departments and try again another day.")
        else:
            print(f"You received {points}. Based on this algorithm, you should consider majoring in {major_recommendation}. Good luck!")

def greet() -> None:
    """Game greeting and discovery of player name."""
    global player
    print(f"Welcome to Carolina Major Quiz? This quiz will recommend one of the popular UNC majors based on your answers to a few simple question. Although it is points based, the goal is to answer accurately as possible to fall in a point range that will coorelate with a major.")
    player = input("Who is playing today? ")
    print(f"Pleasure to meet you {player}! Let's get started!")


def bach_art() -> None:
    """A function for identified BA pursuants that changes the global point based of off the responses to question. Ranges for questions differ between BA and BS to ensure major reccomendation falls within respective interest in BA or BS."""
    global points
    points = 0
    print("You appear to be interested in a Bachelor of Arts degree. Let's choose a BA major based on your answers to a few questions. Please answer with whole numbers (integer).")
    question_1: int = int(input("On a scale of 6 to 10, how interested are you in studying abroad or studying different cultures? "))
    points += question_1
    question_2: int = int(input("On a scale of 6 to 10, how frightened would you be to incorporate math, statistics or science into your studies? "))
    points += question_2
    question_3: int = int(input("On average, how many hours a night do you plan to sleep in college (Answers should be reasonably inbetween 3 to 12? "))
    points += question_3
    question_4: int = int(input("On a scale of 6 to 10, do you deal with stress/anxiety well (6 - I eat stress for breakfast, 10 - hell no?) "))
    points += question_4
    question_5: int = int(input("From a scale of 6 to 10, (10 - loves papers, 6 - loves exams)? "))
    points += question_5
    question_6: int = int(input ("On a scale from 6 to 10, how willing are you to spend a lot of time reading books, academic journals, and more? "))
    points += question_6



def bach_sci() -> None:
    """A function for identified BS pursuants that changes the global point based of off the responses to question. Ranges for questions differ between BA and BS to ensure major reccomendation falls within respective interest in BA or BS."""
    global points
    points = 0
    print("You appear to be interested in a Bachelor of Science degree. Let's choose a BS major based on your answers to a few questions.")
    question_1: int = int(input("On a scale of 1 to 5, how familiar/confortable are you with coding (python, java, R-studio, etc.)? "))
    points += question_1
    question_2: int = int(input("On a scale of 1 to 5, how willing are you to learn to code or use statistical models? "))
    points += question_2
    question_3: int = int(input("On average, how many hours a night do you plan to sleep in college (Answers should be reasonably inbetween 3 to 12? "))
    points += question_3
    question_4: int = int(input("On a scale of 1 to 5, do you deal with stress/anxiety well (5 - I eat stress for breakfast, 10 - hell no?) "))
    points += question_4
    question_5: int = int(input("On a scale of 1 to 5, would you be willing to work in a health sciences capacity (doctor, nurse, technician)? "))
    points += question_5
    question_6: int = int(input("On a scale of 1 to 5, would you like to spend a lot of time in class? "))
    points += question_6

def indec() -> None:
    "For students that decide to test fate, this function will generate a number within the range I have set for other dunctions so that a random major can be decided."
    global points
    points = 0
    range_min_bs: int = 8
    range_max_ba: int = 62
    from random import randint
    points = randint(range_min_bs, range_max_ba)


def final_rec(final_score: int) -> str:
    "A function that takes a number as an input, discovers where it falls in a range of values, and returns an explict recommendation based of off the range in which contained the number."
    global major_recommendation
    range_min_bs: int = 8
    math_cs_max: int = 16
    stats_econ_max: int = 24
    range_max_bs: int = 32
    range_min_ba: int = 33
    psych_soci_max: int = 42
    busi_econ_max: int = 51
    range_max_ba: int = 62
    if points < range_min_bs:
        major_recommendation = "Undecided"
        return major_recommendation    
    if points >= range_min_bs and points <= range_max_bs:
        if points <= math_cs_max:
            major_recommendation = f"Mathematics {RULER}, Physics {MAGNET}, Engineering {BOLT}, or Computer Science {LAPTOP}"
        if points > math_cs_max and points <=stats_econ_max:
            major_recommendation = f"Statistics {ABACUS} or Economics(BS) {CHART}"
        if points > stats_econ_max:
            major_recommendation = f"Biology {HELIX}, Chemistry {TUBE}, Nursing {HOSPITAL}, or Biomechanics {ARM}"
    if points >= range_min_ba and points <= range_max_ba :
        if points <= psych_soci_max:
            major_recommendation = "Psychology or Sociology"
        if points > psych_soci_max and points <= busi_econ_max:
            major_recommendation = f"Business Administration {BRIEFCASE}, Communications {MAIL} or Economics(BA) {CHART}"
        if points > busi_econ_max:
            major_recommendation = f"Language Studies {SPEAKER}, Journalism {NEWSPAPER}, or Global Studies {MAP}"
    if points > range_max_ba:
        print(f"Wow, you recieved a score of {points}, you must sleep a lot {SLEEP}. Maybe college isn't for you! Teachers frown upon sleeping in class.")
        major_recommendation = "Undecided"
    return major_recommendation


if __name__ == "__main__":
    main()
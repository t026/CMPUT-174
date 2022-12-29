import random
import time

def read_spells(filename: str) -> list[str]:
    """
    Reads a list of spells from a file and returns a list of spells.
    """
    with open(filename, "r") as f:
        return f.readlines()  #.readlines() returns a list of all lines in the file.
 
def get_random_spell(spells: list[str]) -> str:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """
    return random.choice(spells).lower().strip()  #.rstrip() removes \n from the string.

 

# Version 1 code here

def display_header():
    """
    Displays header as follows:
    ############################################################
    Harry Potter Typing Trainer
    ############################################################
    """
    print(f"{'#'*60}\nHarry Potter Typing Trainer\n{'#'*60}")
def display_instructions():
    """
    Displays instructions from instructions.txt
    """
    with open("instructions.txt", "r") as f:
        for line in f:
            print(line.rstrip())  #prints every line in the file and removes the \n
def display_feedback(spell: str, user_input: str):
    """
    Displays feedback (correct or incorrect) to the user.
    """
    if user_input.lower() == spell:
        print("Correct!")
    else:
        print(f"Incorrect!\nThe spell was: {spell}")


# Version 2 code here

def play_again() -> bool:
    """
    Asks the user if they want to play again
    Returns True if the user enters Y or y, False otherwise
    """
    user_input = input("Do you want to practice more? (y/n)\n")
    return user_input.lower() == 'y'  #returns a boolean expression

def get_user_input(spell: str) -> (str, float):
    """
    Gets input from the user
    Returns the input and the time it took the user to type the input
    """
    start = time.time()
    print(f"Type the following spell: {spell}")
    user_input = input().lower()
    user_time = round(time.time() - start, 2)
    print(f"Result: {user_time} seconds (goal: {get_target_time(spell)} seconds).")
    return user_input, user_time

def get_target_time(spell: str) -> float:
    """
    Returns the target time to type the spell.
    """
    return round(len(spell)*0.3,2)  #returns the length of the spell * 0.3
def calculate_points(spell: str, user_input: str, user_time: float) -> int:
    """
    Calculates the points that the user gets.
    spell: The spell that the user is typing.
    user_input: The input that the user typed.
    user_time: The time that the user took to type the input.
    """
    if user_input.lower() == spell:
        target_typing_time = get_target_time(spell)
        if user_time <= target_typing_time:
            added_score = 10
        elif user_time <= target_typing_time*1.5:
            added_score = 6
        elif user_time <= target_typing_time*2:
            added_score = 3
        else:
            added_score = 1
    else:
        added_score = -5 #removes 5 if incorrect word is typed
    return added_score
def main() -> None:
    """
    Main program.
    Do all of the stuff that tonly needs to be done once first, then start a while loop.
    Creates a flag that initially is True, then catches th value of play_again()
    """
    spells = read_spells('spells.txt')
    display_header()
    display_instructions()
    flag = True
    score = 0
    while flag: #same as while True for initial loop
        spell = get_random_spell(spells)
        user_input = (get_user_input(spell))  #this is a tuple
        display_feedback(spell, user_input[0])  
        points = calculate_points(spell, user_input[0], user_input[1])
        score += points  #adds added score to the score variable
        print(f"You get {points} points! Your score is: {score}")
        flag = play_again() #if true continues loop, if false breaks loops
    print(f"Your final score is: {score}")
main()
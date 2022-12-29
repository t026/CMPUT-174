
'''
I imported the random module to find a random index in the list for the get_random_spell() function.
'''
import time
import random
def read_spells(filename: str) -> list[str]:
    #Opens the file using the 'with' keyword and returns a list of all of the lines in the file.
    with open(filename, "r") as f:
        return f.readlines()
 
def get_random_spell(spells: list[str]) -> str:
    '''
    .strip() removes \n from each line
    .lower() converts it to lower case
    '''
    return spells[random.randint(0, len(spells)-1)].strip().lower()

def display_header():
    #I created a string that consists of 60 #'s and printed it along the message.
    hashes = '#'*60
    print(f"{hashes}\nHarry Potter Typing Trainer\n{hashes}")

def display_instructions():
    #opens the file "instructions.txt" and prints every line using the strip() function to remove \n
    with open("instructions.txt", "r") as file:
        for line in file:
            print(line.strip())

def display_feedback(spell: str, user_input: str, score : int, user_time : float ) -> int:
    '''
    checks if the lower case values for each string matches and prints the appropriate value.
    I edited this function to take in the score as a parameter and adjusts its value based on the user's input
    I then returned the score value.
    '''
    added_score = calculate_points(spell, user_input, user_time)
    score += added_score
    if spell.lower() == user_input.lower(): 
        print(f"Correct!\nYou get {added_score} points! Your score is {score}")
    else:
        print(f"Incorrect!\nThe correct spell was: {spell}\nYou lose! Your score is {score}")
    return score

def play_again() -> bool:
    """
    Asks the user if they want to play again
    Returns True if the user enters Y or y, False otherwise
    I used the == operation to return True or False and I used the .lower() function so that the case doesn't matter
    """
    user_input = input('Do you want to practice more? (y/n)\n')
    return user_input.lower() == "y"

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
    return len(spell) * 0.3

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
        added_score = -5
    return added_score


    

def main() -> None:
    """
    Main program.
    I created a score variable of type int and a flag variable of type bool
    The flag variable is responsible for the while loop, and I gave flag the value of the play_again function so that it remains true or false based on user input
    i called the display_feedback with the score variable to change it's value.
    """
    score = 0
    flag = True
    display_header()
    display_instructions()
    spells = read_spells('spells.txt')
    while flag:
        spell = get_random_spell(spells)
        user_input = (get_user_input(spell))
        score = display_feedback(spell, user_input[0], score, user_input[1])  
        flag = play_again()
    print(f"Your final score is: {score}.")

main()
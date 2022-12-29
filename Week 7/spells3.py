'''
I imported the random module to find a random index in the list for the get_random_spell() function.
'''
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

def get_user_input(spell: str) -> str:
    #Takes and returns the user input
    user_input = input(f"Type the following spell: {spell}\n")
    return user_input

def display_feedback(spell: str, user_input: str, score : int) -> int:
    '''
    checks if the lower case values for each string matches and prints the appropriate value.
    I edited this function to take in the score as a parameter and adjusts its value based on the user's input
    I then returned the score value.
    '''
    if spell.lower() == user_input.lower():
        score += 10
        print(f"Correct!\nYou get 10 points! Your score is {score}")
    else:
        score -= 5
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
        user_input = get_user_input(spell)
        score = display_feedback(spell, user_input, score)  
        flag = play_again()
    print(f"Your final score is: {score}.")


 
main()
import random
def read_spells(filename: str) -> list[str]:
    """
    Reads a list of spells from a file and returns a list of spells.
    """
    with open(filename, "r") as f:
        return f.readlines()
 
def get_random_spell(spells: list[str]) -> str:
    """
    Returns a random spell from a list of spells, converted to lowercase.
    """
    return random.choice(spells).lower().rstrip()

 

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
            print(line.rstrip())
def get_user_input(spell: str) -> str:
    """
    Gets the spell as input from the user and returns it.
    """
    user_input = input(f"Type the following spell: {spell}\n")
    return user_input
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
    return user_input.lower() == 'y'


def main() -> None:
    """
    Main program.
    """
    spells = read_spells('spells.txt')
    display_header()
    display_instructions()
    # TODO: Implement the game loop (call play_again())
    # TODO: Implement scoring system
    # After the game is over, display the final score
    flag = True
    score = 0
    while flag:
        spell = get_random_spell(spells)
        user_input = get_user_input(spell)
        display_feedback(spell, user_input)
        if user_input == spell:
            score += 10
            print(f"You get 10 points! Your score is: {score}")
        else:
            score -= 5
            print(f"You lose! Your score is {score}")
        flag = play_again()
    print(f"Your final score is: {score}")
main()
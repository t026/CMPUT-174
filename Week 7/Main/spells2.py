'''
I imported the random module to find a random index in the list for the get_random_spell() function.
'''
import random
def read_spells(filename: str) -> list[str]:
    #Opens the file using the 'with' keyword and returns a list of all of the lines in the file.
    with open(filename, "r") as f:
        return f.readlines()
 
def get_random_spell(spells: list[str]) -> str:
    #returns a random element between in the list converted to lower case.
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

def display_feedback(spell: str, user_input: str):
    #checks if the lower case values for each string matches and prints the appropriate value.
    if spell.lower() == user_input.lower():
        print("Correct!")
    else:
        print(f"Incorrect!\nThe correct spell was: {spell}")

def main() -> None:
    """
    Main program.
    """
    spells = read_spells('spells.txt')
    spell = get_random_spell(spells)
    display_header()
    display_instructions()
    user_input = get_user_input(spell)
    display_feedback(spell, user_input)



main()

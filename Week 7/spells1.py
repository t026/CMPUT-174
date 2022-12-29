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
    return spells[random.randint(0, len(spells)-1)].lower()

 
def main() -> None:
    spells = read_spells('spells.txt')
    print('Harry Potter Keyboard Trainer')
    spell = get_random_spell(spells)
    print(spell)

main()


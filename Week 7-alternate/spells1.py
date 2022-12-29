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
    return random.choice(spells).lower()

 
def main() -> None:
    """
    Main program.
    """
    spells = read_spells('spells.txt')
    print('Harry Potter Keyboard Trainer')
    spell = get_random_spell(spells)
    print(spell)

main()


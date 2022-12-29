import random

class Pokemon:
    def __init__(self, name, attack, defense, max_health, current_health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.current_health = current_health

    def __str__(self) -> str:
        """
        Return a string representation of the Pokemon.
        """
        return f"{self.name} (health: {self.current_health}/{self.max_health})"

    def lose_health(self, amount: int) -> None:
        """
        Lose health from the Pokemon.
        """
        if amount > 0:
            if amount < self.max_health:
                self.current_health -= amount
            else:
                self.current_health = 0

    def is_alive(self) -> bool:
        """
        Return True if the Pokemon has health remaining.
        """
        return self.current_health > 0

    def revive(self) -> None:
        """
        Revive the Pokemon.
        """
        self.current_health = self.max_health

def read_pokemon_from_file(filename: str) -> list[Pokemon]:
    """
    Read a list of Pokemon from a file.
    """
    pokemon_list = []
    with open (filename, 'r') as file:
        file_list = file.readlines()
    for i in range(1, len(file_list)):
        line = file_list[i].strip().split("|")
        pokemon_list.append(Pokemon(line[0], line[1], line[2], line[3], line[3]))
    return pokemon_list

def main():
    """
    Battle of two Pokemon
    """
    pokemon_list = read_pokemon_from_file("all_pokemon.txt")
    while True:
        i = random.randint(0, len(pokemon_list))
        j = random.randint(0, len(pokemon_list))
        if i != j:
            break
    print(f"Welcome, {pokemon_list[i]} and {pokemon_list[j]}!")
if __name__ == '__main__':
    main()
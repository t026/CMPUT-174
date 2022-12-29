import random

class Pokemon:
    def __init__(self, name, attack, defense, max_health, current_health):  
        self.name = name
        self.attack = int(attack)
        self.defense = int(defense)
        self.max_health = int(max_health)
        self.current_health = int(current_health)

    def __str__(self) -> str:
        """
        Return a string representation of the Pokemon.
        """
        string = f"{self.name} (health: {self.current_health}/{self.max_health})"
        return string

    def lose_health(self, amount: int) -> None:
        """
        Lose health from the Pokemon.
        """
        if amount > 0 and amount < self.current_health:
            self.current_health -= amount
        elif amount >= self.current_health:
            self.current_health = 0

    def is_alive(self) -> bool:
        """
        Return True if the Pokemon has health remaining.
        """
        if self.current_health > 0:
            return True  
        return False

    def revive(self) -> None:
        """
        Revive the Pokemon.
        """
        self.current_health = self.max_health 
        print(f"{self} has been revived.")

    def attempt_attack(self, other: "Pokemon") -> bool:
        """
        Attempt an attack on another Pokemon.
        This method can either return a bool, or return nothing
        (depends on your implementation)
        """
        luck = (random.randint(7, 13))/10
        damage = round(luck * self.attack)  
        effective_damage = damage - other.defense
        print(f"{self.name} attacks {other.name} for {damage} damage.")  
        if effective_damage > 0:  
            other.lose_health(effective_damage)
            print(f"Attack is successful. {other.name} has {other.current_health} health remaining!")
        else:
            print("Attack is blocked!")
        return other.is_alive()

def read_pokemon_from_file(filename: str) -> list[Pokemon]:
    """
    Read a list of Pokemon from a file.
    """
    list_pokemon = []
    file = open(filename, 'r', encoding="utf-8")  #encoding allows special characters to be read
    all_pokemon = file.readlines()
    file.close()
    num_of_pokemon = len(all_pokemon) - 1
    all_pokemon.pop(0)
    for i in range(0, num_of_pokemon):
        pokemon_details = all_pokemon[i].strip()
        pokemon_details = pokemon_details.split("|")
        pokemon_stats = {'name' : pokemon_details[0], 'attack' : pokemon_details[1], 'defense' : pokemon_details[2], 'health' : pokemon_details[3]}
        list_pokemon.append(Pokemon(pokemon_stats['name'], pokemon_stats['attack'], pokemon_stats['defense'], pokemon_stats['health'], pokemon_stats['health']))
    return list_pokemon

def coinflip():
    mylist = ['a', 'b']
    return random.choice(mylist) == mylist[0]

def main():
    """
    Battle of two Pokemon
    """
    list_of_pokemon = read_pokemon_from_file("all_pokemon.txt") 
    i = random.choice(list_of_pokemon)
    j = random.choice(list_of_pokemon)
    while i == j:
        j = random.choice(list_of_pokemon)
    print(f"Welcome, {i} and {j}!")
    round = 0
    while round < 10:
        round += 1 
        print(f"\nRound {round} begins. {i} and {j}")
        if i.attempt_attack(j): 
            if not j.attempt_attack(i):
                if coinflip():
                    i.revive()
                else:
                    print(f"{j.name} has won in {round} rounds!")
                    round = 0
                    break
        else:  
            if coinflip(): 
                j.revive()
            else:
                print(f"{i.name} has won in {round} rounds!")
                round = 0
                break
    if round >= 10:  
        print(f"Its a tie between {i} and {j}") 

if __name__ == '__main__':
    main()
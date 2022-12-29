'''
Lab 10 Version 4
Name : Tanishq
Description : Implements attack function and game loop in main function
'''
import random

class Pokemon:
    def __init__(self, name, attack, defense, max_health, current_health):  #assigns parameters to attributes of the object
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.current_health = current_health

    def __str__(self) -> str:
        """
        Return a string representation of the Pokemon.
        """
        return f"{self.name} (health: {self.current_health}/{self.max_health})"  #returns a string in the correct format so it can be printed

    def lose_health(self, amount: int) -> None:
        """
        Lose health from the Pokemon.
        """
        if amount > 0:  #checks if amount is positive
            if self.current_health - amount <= 0:  #checks if amount is more than health
                self.current_health = 0  #sets to 0 if amount is more than current health
            else:
                self.current_health -= amount  #subtracts amount from current health if amount is not greater than current health

    def is_alive(self) -> bool:
        """
        Return True if the Pokemon has health remaining.
        """
        return self.current_health > 0  #returns True if self.current_health is greater than 0

    def revive(self) -> None:
        """
        Revive the Pokemon.
        """
        self.current_health = self.max_health  #sets current health to max health

    def attempt_attack(self, other: "Pokemon") -> bool:
        """
        Attempt an attack on another Pokemon.
        This method can either return a bool, or return nothing
        (depends on your implementation)
        """
        luck = round(random.uniform(0.7, 1.3),1)  #calculates luck using random.uniform to generate float values between 0.7 and 1.3 that are then rounded to 1 decimal place
        damage = round(luck * float(self.attack))  #damage calculation
        print(f"{self.name} attacks {other.name} for {damage} damage.")  
        if damage > int(other.defense):  #checks if attack is successful
            damage_dealt = damage - other.defense  #calculates damage dealt by subtracting defense from damage
            other.lose_health(damage_dealt)
            print(f"Attack is successful. {other.name} has {other.current_health} health remaining!")
        else:
            print("Attack is blocked!")

def read_pokemon_from_file(filename: str) -> list[Pokemon]:
    """
    Read a list of Pokemon from a file.
    """
    pokemon_list = []
    with open (filename, 'r', encoding="utf-8") as file:  #encoding allows special characters to be read
        file_list = file.readlines()
    for i in range(1, len(file_list)):  #starts at 1 as the first line is a template and not a pokemon
        line = file_list[i].strip().split("|")
        pokemon_list.append(Pokemon(line[0], int(line[1]), int(line[2]), int(line[3]), int(line[3])))  #current health = max health at the start
    return pokemon_list

def main():
    """
    Battle of two Pokemon
    """
    pokemon_list = read_pokemon_from_file("all_pokemon.txt")  #reads pokemon
    while True:
        pokemon_1 = random.choice(pokemon_list)
        pokemon_2 = random.choice(pokemon_list)
        if pokemon_1 != pokemon_2:
            break  #keeps on looping until they are different 
    print(f"Welcome, {pokemon_1} and {pokemon_2}!")
    #game loop
    round = 0
    while round < 10:
        round += 1  #increments round at the start
        print(f"\nRound {round} begins. {pokemon_1} and {pokemon_2}")
        pokemon_1.attempt_attack(pokemon_2)
        if pokemon_2.is_alive():  #checks if alive
            pokemon_2.attempt_attack(pokemon_1)
            if not pokemon_1.is_alive():  #50 chance to be revived
                if random.randint(1,2) == 2:  #50% chance for it to be 2.
                    pokemon_1.revive()
                    print(f"{pokemon_1} has been revived.")
                else:
                    print(f"{pokemon_2.name} has won in {round} rounds!")
                    round = 50  #sets round way above 10 to break loop
        else:  #50% chance to revive if not alive
            if random.randint(1,2) == 2:  #50% chance for it to be 2
                pokemon_2.revive()
                print(f"{pokemon_2} has been revived.")
            else:
                print(f"{pokemon_1.name} has won in {round} rounds!")  
                round = 50  #sets round way above 10 break loop
    if round == 10:  
        print(f"Its a tie between {pokemon_1} and {pokemon_2}")  #it can only be a tie
    
if __name__ == '__main__':
    main()
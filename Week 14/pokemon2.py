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

def main():
    """
    Battle of two Pokemon
    """
    pokemon1 = Pokemon("Pikachu", 55, 40, 35, 35)
    pokemon2 = Pokemon("Bulbasaur", 49, 49, 45, 45)
    print(f"Welcome, {pokemon1} and {pokemon2}!")

if __name__ == '__main__':
    main()
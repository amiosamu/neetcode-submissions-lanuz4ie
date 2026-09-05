class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        self.name = name
        self.power = power
        self.health = health

    # Attack method
    def attack(self):
        print(f"{self.name} attacks with {self.power}!")

    # Heal method
    def heal(self, points: int):
        self.health += points
        print(f"{self.name} heals {points} points. New health: {self.health}.")


# Create superhero instance
catwoman = SuperHero("Catwoman", "Agility", 120)

# Use the attack() and heal() methods
catwoman.attack()
catwoman.heal(10)
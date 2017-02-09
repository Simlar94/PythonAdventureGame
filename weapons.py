from random import randint
from characteristics import Characteristics


class Weapon(Characteristics):
    def __init__(self, name, damage, description):
        self.description = description
        super().__init__(name, self, damage)


staff = Weapon("Staff of Darkness", randint(3, 6), "Damage: 3-6")
dagger = Weapon("Dagger of Youth", randint(2, 7), "Damage: 2-7")
sword = Weapon("Sword of Wisdom", randint(0, 9), "Damage: 0-9")
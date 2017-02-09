from random import randint
from characteristics import Characteristics


class Enemy(Characteristics):  # Base class for all enemies.
    def __init__(self, name, hp, damage, difficulty):
        self.difficulty = difficulty
        super().__init__(name, hp, damage)


vampireeasy = Enemy("Edward", 25, randint(0, 25), "Easy")
vampiremedium = Enemy("Elena", 50, randint(0, 50), "Medium")
vampirehard = Enemy("Stefan", 75, randint(0, 75), "Hard")
vampireboss = Enemy("Damon", 100, randint(0, 100), "Expert")
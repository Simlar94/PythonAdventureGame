from player import *
from enemies import Enemy


class Attack(Enemy):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)

    def playerattacked(self):
        playerobj.hp -= self.damage  # Player's HP - Enemy's damage.

    def enemyattacked(self):
        self.hp -= playerobj.damage  # Enemy's HP - Player's HP.

    def checklife(self):
        if playerobj.hp < 1:
            print("You have been defeated...")
        elif self.hp < 1:
            print("You have defeated " + self.name + "!")


def attackplayer(whichenemy):
    Attack.playerattacked(whichenemy)


def attackenemy(whichenemy):
    Attack.enemyattacked(whichenemy)




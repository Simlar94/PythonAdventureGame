from characteristics import Characteristics


class Player(Characteristics):
    def __init__(self, name, hp, damage, healingability):
        self.healingability = healingability
        super().__init__(name, hp, damage)

    def healplayer(self):
        playerobj.hp = playerobj.hp + playerobj.healingability  # Heals player.


playerobj = Player("", 100, 10, 10)
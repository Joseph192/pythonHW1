class Dragon:
    health = 2000
    mana = 400
    attackDamage = 50
    magicDamage = 100
    armor = 1000
    def __init__(self, color, title, weight, height):
        self.color = color
        self.title = title
        self.weight = weight
        self.height = height

    def fireBreath(self):
        self.mana = self.mana - 50

    def ascension(self):
        self.health = self.health + 1000

    def restorationBlast(self):
        self.health = self.health + 500

    def chaosShield(self):
        self.armor = self.armor * 2


class Knight:
    health = 1000
    attackDamage = 60
    armor = 500

    def __init__(self, firstName, lastName, sword):
        self.firstName = firstName
        self.lastName = lastName
        self.sword = sword

    def phantomFighters(self):
        self.health = self.health * 1.5

    def powerBreak(self):
        self.attackDamage = self.attackDamage * 2
        self.armor = self.armor / 2

    def onslaught(self):
        self.health = self.health - 100


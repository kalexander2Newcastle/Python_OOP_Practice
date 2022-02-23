class TradingCard:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def sethp(self, health):
        self.hp = health

    def gethp(self):
        return self.hp

    def setAttack(self, attack):
        self.attack = attack

    def getAttack(self):
        return self.attack

    def setDefense(self, defense):
        self.defense = defense

    def getDefense(self):
        return self.defense

    def __str__(self):
        return str(TradingCard.getName(self)) + "," + str(TradingCard.gethp(self)) + "," + str(TradingCard.getAttack(self)) + "," + str(TradingCard.getDefense(self))



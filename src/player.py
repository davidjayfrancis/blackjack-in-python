class Player:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank

    def __str__(self):
        return f"name: {self.name}, bank: {self.bank}"

    def addFunds(self, amt):
        self.bank += amt

    def removeFunds(self, amt):
        self.bank -= amt
    
    def taunt(self):
        return f"I'm think you're going to lose, friend."

    def checkBet(self, amt):
        if amt >= self.bank:
            return False
        return True
    
    def getBank(self):
        return self.bank

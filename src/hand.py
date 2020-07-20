class Hand:
    def __init__(self, stay=False):
        self.stay = stay
        self.cards = []
        
    def drawCard(self, deck):
        self.cards.append(deck.dealCard())
    
    def displayHand(self):
        return f"{[f'{card.num}{card.face},' for card in self.cards]}"
        
    # Corner case to be resolved:
    # --> Ace Ace Jack will fail (e.g. 11 + 1 + 10 = 22)
    def calculateScore(self):
        values = {
            'Ace': 1,
            2:2,
            3:3,
            4:4,
            5:5,
            6:6,
            7:7,
            8:8,
            9:9,
            10:10,
            'Jack': 10,
            'Queen': 10,
            'King': 10
        }
        aces = []
        total = 0
        for card in self.cards:
            if card.num == 'Ace':
                aces.append(card)
            else:
                total += values[card.num]
        for ace in aces:
            if total <= 10:
                total += 11
            else:
                total += 1
        return total
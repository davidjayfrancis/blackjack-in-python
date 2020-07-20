from card import Card
import random
class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ['\u2665',"\u2660",'\u2663','\u2666']
        self.values = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King' ]
        for i in range(len(self.values)):
            for j in range(len(self.suits)):
                self.cards.append(Card(self.values[i], self.suits[j]))
    
    def showDeck(self):
        for i in self.cards:
            print(f"{i.num} of {i.face}")
        
    def shuffle(self, x):
        for i in range(x):
            index1 = random.randrange(52)
            index2 = random.randrange(52)
            card1 = self.cards[index1]
            card2 = self.cards[index2]
            self.cards[index1] = card2
            self.cards[index2] = card1
    
    def dealCard(self):
        return self.cards.pop()
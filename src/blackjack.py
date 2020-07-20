class Card:
    def __init__(self, num, face):
        self.num = num
        self.face = face
        
    def __str__(self):
        print(f"{self.num} of {self.face}")

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
    
    import random
    
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
    
class Hand:
    def __init__(self, stay=False):
        self.stay = stay
        self.cards = []
        
    def drawCard(self, deck):
        self.cards.append(deck.dealCard())
    
    def displayHand(self):
        return f"current hand is: {[f'{card.num}{card.face},' for card in self.cards]}"
        
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
            
class Player:
    def __init__(self, name, bank):
        self.name = name
        self.bank = bank


# create a gameloop
import random

# deal_cards to dealer and player
def startGame():
    deck = Deck()
    deck.shuffle(1000)
    player = Hand()
    dealer = Hand()

    player.drawCard(deck)
    dealer.drawCard(deck)
    player.drawCard(deck)
    dealer.drawCard(deck)
    
def displayHands():
    print(f'Your {player.displayHand()} for a total of {player.calculateScore()}')
    print(f"Dealer {dealer.displayHand()} for a total of {dealer.calculateScore()}")


def determineWinner(player, dealer):
    if dealer.calculateScore() > 21: 
        print("Congratulations, you win!")
    elif player.calculateScore() > 21: 
        print('You lose!')
    elif player.calculateScore() > dealer.calculateScore():
        print("Congrats, you win!")
    elif dealer.calculateScore() > player.calculateScore(): 
        print("you lose!")
    else:
        print("it's a tie! wow that is rare : )")

def dealerMove():
    while dealer.calculateScore() <17:
        print("dealer draws a card...")
        dealer.drawCard(deck)
        print(f"dealer draws a {dealer.cards[-1].num}{dealer.cards[-1].face}.")
        print(f"dealers hand is now {dealer.displayHand()} for a total of {dealer.calculateScore()}")
        if dealer.calculateScore() >= 17 and dealer.calculateScore() <= 21:
            print(f"dealer decides to stay at {dealer.calculateScore()}")
        if dealer.calculateScore() > 21:
            print("Dealer busts! You win!")
#             break
            determineWinner(player, dealer)
            
def playerMove():
    while player.calculateScore() <= 21 and player.stay == False:
        move = input("what you would you like to do, hit (h) or stay (s)? (Or press 'q' to quit))")
        if move == 's':
            player.stay = True
        elif move == 'h':
            print("you draw a card...")
            player.drawCard(deck)
            print(f"you draw a {player.cards[-1].num}{player.cards[-1].face}")
            print(f"Your hand is now {player.displayHand()} with a value of {player.calculateScore()}")
        elif move == 'q':
            print("OK Seeya cowboy!")
            global game_state
            print(game_state)
            game_state = False
            print(game_state)
            break
    

def game_ends():
    ipt = input("Would you like to play again? (y/n)")
    if ipt == 'n':
        global game_state
        print("Thank you for playing. Until the next time cowboy!")
        game_state = False
    if 'y': 
        pass # need to think how to reset hand
    else:
        print("I don't recognize that command. please enter 'y' or 'n'")


print("Welcome to BlackJack!!")
game_state = True
while game_state == True:
    
    print("shuffling the deck...\n")
    deck = Deck()
    deck.shuffle(1000)
    print("dealing the cards...\n")
    player = Hand()
    dealer = Hand()

    player.drawCard(deck)
    dealer.drawCard(deck)
    player.drawCard(deck)
    dealer.drawCard(deck)
    
    displayHands()
    
    while (game_state == True) and (player.calculateScore() <= 21) and (dealer.calculateScore() <=21) and (player.stay is not True) and (dealer.stay is not True):
        dealerMove()
        playerMove()
    determineWinner(player, dealer)
    game_ends()
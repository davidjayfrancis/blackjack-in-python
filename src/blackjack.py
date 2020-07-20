from card import Card
from deck import Deck
from hand import Hand
from player import Player

# create a gameloop
import random
import os

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
    print("...........................................")
    print(f'Your hand: {player.displayHand()} for a total of {player.calculateScore()}')
    print(f"Dealer's hand: {dealer.displayHand()} for a total of {dealer.calculateScore()}")
    print("...........................................\n")


def determineWinner(player, dealer):
    if dealer.calculateScore() > 21: 
        print("Congratulations, you win!")
        print("...................")
        print(f"You won ${bet}")
        p1.addFunds(bet)
        p1.addFunds(bet)
        print(f"Your current bank is {p1.bank}")
        print("...................\n")
    elif player.calculateScore() > 21: 
        print('You lose!')
    elif player.calculateScore() > dealer.calculateScore():
        print("Congrats, you win!")
        print("...................")
        print(f"You won ${bet}")
        p1.addFunds(bet)
        p1.addFunds(bet)
        print(f"Your current bank is {p1.bank}")
        print("...................\n")
    elif dealer.calculateScore() > player.calculateScore(): 
        print("you lose!")
    else:
        print("it's a tie! wow that is rare : )")
        p1.addFunds(bet)

def dealerMove():
    while dealer.calculateScore() <17:
        print("dealer draws a card...")
        dealer.drawCard(deck)
        print(f"dealer draws a {dealer.cards[-1].num}{dealer.cards[-1].face}.")
        print('...............................')
        print(f"dealers hand is now {dealer.displayHand()} for a total of {dealer.calculateScore()}")
        print('...............................\n')
        if dealer.calculateScore() >= 17 and dealer.calculateScore() <= 21:
            print(f"dealer decides to stay at {dealer.calculateScore()}")
            dealer.stay = True
        if dealer.calculateScore() > 21:
            print("Dealer busts! You win!")
            player.stay = True
    
            
def playerMove():
    while player.calculateScore() <= 21 and player.stay == False:
        move = input("what you would you like to do, hit (h) or stay (s)?\n......................\n")
        if move == 's':
            player.stay = True
        elif move == 'h':
            print("you draw a card...")
            player.drawCard(deck)
            print(f"you draw a {player.cards[-1].num}{player.cards[-1].face}")
            print('............................................')
            print(f"Your hand is now {player.displayHand()} with a value of {player.calculateScore()}")
            print(f"Dealer's hand is now {dealer.displayHand()} with a value of {dealer.calculateScore()}")
            print('............................................\n')
    
def game_ends():
    ipt = input("Would you like to play again? (y/n)")
    if ipt == 'n':
        global game_state
        print("Thank you for playing. Until the next time cowboy!")
        game_state = False
    if 'y': 
        os.system('clear')
    else:
        print("I don't recognize that command. please enter 'y' or 'n'")


print("Welcome to BlackJack!!")
name = input("What's your name, friend?")
bank = input("and how much are we playing with today, friend?")
p1 = Player(name, bank)

game_state = True
while game_state == True:
    
    bet = input("How much would you like to bet? ($10 minimum)")
    if p1.checkBet(bet):
        p1.removeFunds(bet)
        print(f"${bet} removed from funds. You have ${p1.bank} left.")

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
    
    while (game_state == True) and (player.calculateScore() <= 21) and (dealer.calculateScore() <=21) and ((player.stay is not True) and (dealer.stay is not True)):
        dealerMove()
        playerMove()
    determineWinner(player, dealer)
    game_ends()
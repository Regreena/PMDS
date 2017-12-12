# Author: Regina Taurino
#
# Unit 5 Assignment 2

# import random to use for shuffle

import random
# assign Card class

# Create constructor with class variables

class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = int(suit)
# Create getters and setters for the values and suits of the cards

    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value

    def getSuit(self):
        return self.suit
#    def setSuit(self,suit):
#        self.suit = suit    
    # Define method to convert the integers to strings when necessary and print the card values and suits.
        
    def showCard(self):
        suitName = ""
        cardName = ""
        if self.suit == 1:
            suitName = "Clubs"
        elif self.suit == 2:
            suitName = "Diamonds"
        elif self.suit == 3:
            suitName = "Hearts"
        elif self.suit == 4:
            suitName = "Spades"
        if self.value == 11:
            cardName = "Jack"
        elif self.value == 12:
            cardName = "Queen"
        elif self.value == 13:
            cardName = "King"
        elif self.value == 14:
            cardName = "Ace"
        else:
            cardName = self.value
            
        print("%s of %s" % (cardName, suitName))
# Create Deck class       
        
class Deck(object):
    # Create constructor    
    def __init__(self):
        # Create empty list for cards
        self.cards = []
        self.Order()
# create method to sort the deck in desired order

    def Order(self):
        sn = ''
        for s in ["1", "2", "3", "4"]:
            if s == 1:
                sn = "Clubs"
            elif s == 2:
                sn = "Diamonds"
            elif s == 3:
                sn = "Hearts"
            elif s == 4:
                sn = "Spades"
            for v in range(2, 15):
                self.cards.append(Card(v,s))
    # Create method to shuffle the deck
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            rand_card = random.randint(0,i)
            self.cards[i], self.cards[rand_card] = self.cards[rand_card], self.cards[i]
                        
    # Create method to list the cards in the deck from top cards to bottom of the deck.         
    def fan(self):
        for c in self.cards:
            c.showCard()
    # Create method to return the value of the card on the top of the deck. Pop removes the card from the deck so there are no repreats.
    def deal(self):
        return self.cards.pop()
    # Create method to return True if the deck is in order and False if it is not.

    def isOrdered(self):
        # Create empty lists so can iterate through them and then compare them
        newList = []
        newValList = []
        newNewList = []
        for c in self.cards:
            newList.append(c)
        for n in newList:
            suitVal = n.getSuit()
            cardVal = n.getValue()
            if cardVal < 10:
                # need to multiply by 10 or else Clubs may appear to be higher value sometimes than Spades.
                suitVal = suitVal*10
            # Concatenate
            newVal = str(suitVal)+str(cardVal)
            # Cast as an integer
            intVal = int(newVal)
            print(newVal)
            n.showCard()
            newValList.append(intVal)
        for check in newValList:
            newNewList.append(check)
        order = "True"
        # Sort list
        newValList.sort()
        # Check the current deck against a sorted deck to see if it is sorted.
        for x in range(len(newValList)):
            if newValList[x] == newNewList[x]:
                order = "True"
            else:
                order = "False"
                break
        print(order)
# Create class for Acey Ducey
class AceyDucey:
    # Create constructor
    def __init__(self):
        # Set wager to 0 and chips to 10 to begin
        self.wager = 0
        self.chips = 10
        # Start the game!
        self.startGame()

    # Define getters and setters for card1, card2, card3, and wager.
    def getCard1(self):
        return self.card1
    def setCard1(self,card1):
        self.card1 = card1

    def getCard2(self):
        return self.card2
    def setCard2(self,card2):
        self.card2 = card2

    def getCard3(self):
        return self.card3
    def setCard3(self,card3):
        self.card3 = card3


    def getWager(self):
        # Get input for wager and check to see if player has enough chips to bet
        wager = input("\nHow many chips would you like to wager? ")
        self.chips = self.chips-int(wager)
    
        while self.chips < 0:
            self.chips = self.chips+int(wager)
            wager = input("You do not have that many chips to bet! Please bet fewer chips: ")
            self.chips = self.chips-int(wager)
        self.setWager(wager)
        
    def setWager(self,wager):
        self.wager = int(wager)
    # Define the rules of the game. If card 3 falls between the high and low card, win and win wagered chips. If lose, lose wager.
    def win(self,card1, card2, card3):
        if card1.getValue() > card2.getValue():
            highCard = card1.getValue()
            lowCard = card2.getValue()

        elif card1.getValue() < card2.getValue():
            highCard = card2.getValue()
            lowCard = card1.getValue()
        # Tie
        else:
            highCard = card1.getValue()
            lowCard = card2.getValue()

        if card3.getValue() < highCard and card3.getValue() > lowCard:
            self.chips = self.chips + (self.wager*2)        

        print("You have %i chips" % (self.chips))
    # Define method to start the game, which begins a round.
    def startGame(self):
        self.round()
    # Define a method to start a round.
    def round(self):
        # Need to call the deck
        deck = Deck()
        # Shuffle the deck
        deck.shuffle()
        # Set counter at 0 so can use to determine when deck has run out of cards before hit error message.
        counter = 0
        # Use while loop to keep game going as long as the player has enough chips and cards.
        while int(self.chips) > 0 and counter < 17:
            # Count up for each loop
            counter = counter + 1
            print("\nYour first card is: ")
            # Deal the first card
            card1 = deck.deal()
            card1.showCard()
            print("\nYour second card is: ")
            # Deal the second card
            card2 = deck.deal()
            card2.showCard()
            # Get the wager from the player
            self.getWager()

            print("\nYour third card is: ")
            # Deal the third card
            card3 = deck.deal()
            card3.showCard()
            # Evaluate cards to see if player has won.
            self.win(card1,card2,card3)
        # Game over!
        print("Thanks for playing!")

        
# Start game!
game = AceyDucey()

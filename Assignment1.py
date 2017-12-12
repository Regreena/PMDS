# Author: Regina Taurino
# Unit 5 Assignment 1

# import random to use for shuffle
import random

# assign Card class
class Card(object):
    # Create constructor with class variables
    def __init__(self, value, suit, suitName):
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
                self.cards.append(Card(v,s,sn))
    # Create method to shuffle the deck
    def shuffle(self):
        for i in range(len(self.cards)-1,0,-1):
            rand_card = random.randint(0,i)
            self.cards[i], self.cards[rand_card] = self.cards[rand_card], self.cards[i]
                        
    # Create method to list the cards in the deck from top card to bottom of the deck.         
    def fan(self):
        for c in self.cards:
            c.showCard()
    # Create method to return the value of the card on the top of the deck.
    def deal(self):
        return self.cards.pop()
    # Create method to return True if the deck is in order and False if it is not.
    def isOrdered(self):
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
            newVal = str(suitVal)+str(cardVal)
            intVal = int(newVal)
            print(newVal)
            n.showCard()
            newValList.append(intVal)
        for check in newValList:
            newNewList.append(check)
        order = "True"
        # Sort list
        newValList.sort()
        # Check the current deck against a sorted deck to see if is ordered.
        for x in range(len(newValList)):
            if newValList[x] == newNewList[x]:
                order = "True"
            else:
                order = "False"
                break
        print(order)
                
            
       



deck = Deck()

deck.shuffle()
card = deck.deal()

#deck.fan()

card.showCard()
card = deck.deal()
card.showCard()
card = deck.deal()
card.showCard()
card = deck.deal()
card.showCard()
card = deck.deal()
card.showCard()
card = deck.deal()
card.showCard()

deck.isOrdered()

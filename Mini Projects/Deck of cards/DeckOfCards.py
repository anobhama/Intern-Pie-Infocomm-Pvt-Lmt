# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 19:42:14 2020

@author: Anobhama
"""
#deck of cards 
#OOPS concepts
import random

class Card(object):
    #constructor
    def __init__(self,cardName,value):
        self.cardName = cardName
        self.value = value
        
    def __str__(self):
        return self.show()
    def __repr__(self):
        return self.show()
    
    #showing the cards present
    def show(self):
        if self.value == 1:
            val = "Ace"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value

        return "{} of {}".format(val, self.cardName)

class Deck(object):
    def __init__(self):
        self.cards = []
        self.buildDeck()
    #building 52 cards of all 4 types of card names
    def buildDeck(self):
        for card in ["spades","clups","diamonds","hearts"]:
            #print(card)
            for value in range(1,14):
                #print(value)
                #print("{} of {}".format(value,card))
                self.cards.append(Card(card,value))
    
    # Display all cards in the deck
    def show(self):
        for card in self.cards:
            print(card.show())
            
    #shuffle the card in the deck
    def shuffleDeck(self,num=1):
        for c in range(num):
            for card in range(len(self.cards)-1,0,-1):
            #print(card)
                rand=random.randint(0,card)
                if card == rand:
                    continue
                self.cards[card],self.cards[rand] = self.cards[rand],self.cards[card]
    
    def drawDeck(self):
        return self.cards.pop()
    
                
class Player(object):
    def __init__(self,name):
        self.name = name
        self.hand = []
    
    #draw the card from the deck
    def drawCard(self,deck,num=1):
        for card in range(num):
            card = deck.drawDeck()
            if card:
                self.hand.append(card)
            else: 
                return False
        return True
    
    #printing player name
    def info(self):
        print ("Hi! My name is {}".format(self.name))
        print("\n")
        return self
    #display the cards in player hand
    def show(self):
        print ("{}'s hand: {}".format(self.name, self.hand))
        return self
    
    def discard(self):
        return self.hand.pop()

n=int(input("enter how much players to be played: "))
for player in range(n):
    name=input("Enter your name: ")
    deck=Deck()
    deck.shuffleDeck()
    player=Player(name)
    player.info()
    player.drawCard(deck,13)
    player.show() 



       
"""
#Testing

#show() in card class    
card = Card("heart",3)
card.show()
# biulding the deck 
#we dont have to call the buildDeck() separately as it already defines in the constructor
deck=Deck()
#checking whether cards are present in the deck
deck.show()
#shuffling the card and printing it
deck.shuffleDeck()
deck.show()
#drawing tje cards from the deck
card= deck.drawDeck()
card.show()
#retrieving a single shuffled card from the deck for a player
deck=Deck()
deck.shuffleDeck()
ano=Player("ano")
ano.drawCard(deck)
ano.show()
"""
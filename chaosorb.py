try:
	import sys
	import random
	import math
	import numbers
	import os
	import getopt
	from socket import *
	from random import shuffle
	
	import game
	
except ImportError, err:
	print "couldn't load module. %s" % (err)
	sys.exit(2)
	
# constant landBase = 25
# constant landDev = 15
# constant landDevAdj = -10
	
class CardPool:
    def init():
        # load up cards.xml
        # parse it into a huge array of cards
        rawCardsData = []   # read the cards.xml file
        cards = []          # the array of parsed cards
        
        for each card in rawCardsData:
            cards.append(Card(card))
            if cards.peek().type == "land"
                self.land.append(cards.peek())
            else:
                self.nonland.append(cards.peek())
            
    def selectRandomNonLand():
        # returns a single card from the set of valid cards that is not a land card.
        # probably will implement this as a while loop, instead of having a non-land dictionary
        pass
        
    def selectRandomLand():
        pass

class Card:
    # cards can be subclassed into permanents and spells, which each have their own subclasses.
    # this should probably happen when we init
    
    def init(carddata):
        # this function will take in the xml element for a card, 
        # and parse it into the various attributes of a card data structure.
        """
    	- mana cost
    	- p/t\
    	- type\
    		- artifact, instant, sorcery, creature, planeswalker, land, enchantment\
    	- color\
    	- subtype\
    		- zombie, etc.\
    	- supertype\
    		- legendary\
    	- array of keyword abilities\
    		- flying\
    		- infect\
    		- swampwalk\
    		- first strike\
    		- trample\
    		- haste\
    		- vigilance\
    		- reach\
    		- flash\
    	"""
        pass

class Population:
    def init(count):
        self.decks = [x for x in range(count) x = Deck()]
    # a collection of decks to be tested against each other, and evolved.

class Deck:
    # a single deck instance to be evaluated.
    # constraints/shortcuts - no sideboard.  goldfishing only.
    def init():
        # generate a deck list.
        #self.landCount = landBase + (random(landDev) + landDevAdj)
        self.decklist = [x for x in range(60-landCount) x = Cards.seletRandomNonland()]
        for x in range(landCount):
            self.decklist.append(Cards.selectRandomLand())
    
    def evaluate(runs):
        # goldfish the deck for runs number of times, and calculate the average turns to lethal.
        # later we'll need more complex evaluation functions, this will greatly overvalue aggro
        
        for i in range(runs):
            totalScore += Game(self).getTurns()
        
        score = totalScore/runs  # low scores are better.  

def main():
    
    cardpool = Cardpool.init()
    
    population = Population.init(10)
    
    
    pass
    
if __name__ == '__main__': main()
class Game:
    # a simulated game of mtg.  for now, goldfish only
    
    def init(scoredDeck):   # later, we will also have a challenger deck
        self.scoredDeck = scoredDeck
        pass
    
    def getTurns():
        #run a game, and return the number of turns to win.
        turns = 0
        
        self.oppLife = 20
        self.oppCards = 60
        self.gameOver = false
        
        self.drawHand()
        
        while !gameOver:
            self.turn()
            turns++
        
        return turns
    
    def drawHand():
        self.hand = []
        shuffle(scoredDeck)
        
        for i in range(7):
            self.Draw() # more clear, less redundant to call off for this
            
    def draw():
        self.hand.append(scoredDeck.pop())
        # note that we are sort of drawing from the bottom of the deck.
        # so anything that interacts with top of deck will need to use last
        # not 0
    
    def turn():
        self.untap()
        self.upkeep()
        self.draw()
        
        self.main1()
        
        self.combat()
        
        self.main2()
        
        self.EOT()
    
    def untap():
        for each perm in self.inPlay:
            perm.untap()
    
    def upkeep():
        runTriggers("upkeep", self.inPlay)
        
        self.priority(False)
    
    def main1():
        self.priority(True)
    
    def combat():
        for each creature in self.creatures:
            # this is not quite right.  doesn't really let us evaluate different combos.
            # we'll need to generate some heuristics later.  this could get combinatoric.
            # for now, we'll just eval for each creature if they could do more damage 
            # if they use an ability instead.
            
            # examples - skirsdag high priest, chosen of markov, thraben doomsayer
            
            # actually, for now, lets skip all that, and just turn em sideways.
            self.attacking.append(creature)
            # for each trigger in creature.triggers contains "attack":
            
             # we're building the list instead of executing here, because the effects may hit all attackers
            runTriggers("attack", self.attacking)
        
        for each creature in self.attacking:
            creature.damage()
    
    def main2():
        self.priority(True)
        
    def EOT():
        discard()
            
    def runTriggers(triggerType, collection):
        triggers = [x for x in collection.triggers if x.trigger == triggerType]
        for each trigger in triggers:
            triggerList.append(trigger)
        for each effect in triggerList
            effect.activate()
            
    def discard():
        while len(self.hand) >= 7:
            for each card in self.hand:
                if card.value < min:
                    min = card.value
                    cur = card
            graveyard.append(self.hand.play(cur))
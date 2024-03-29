class SifterAgent(object):
    def __init__(self,game_object):
        """
        constructor for a SiftAgent
        initializes all necessary data
        """
        self.game = game_object #initial game data 
		self.scored_ global_rack = [] #global rack with current value of all cards [list]
        self.scored_self_rack = [] #agent's own rack, ranked by expected value of cards in rack (min heap)
		self.fuzzy_rack = [] #rack of cards with unknown status, where current value is weighted by probability (max heap)
		self.turn = 0
        self.current_rack_score = -1000
        
		""" available data from game object
        self.game_id = game_id
        self.player_id = player_id
        self.discard_pile = [initial_discard]
        self.other_player_id = other_player_id
        self.current_rack = []
        self.opponent_rack = []
        self.unknown_cards = [] # should be the 59 cards NOT in the discard_pile + current_rack
		"""
    
	def observeOpponentMove(self,move):
        """
        observe the opponent move
        updates card all values
        """
        return
    
	def getAction(self,move):
		"""
		GENERATES THE NEXT MOVE
		-evaluate the goodness of our hand
		-find best fit for card from discard pile 
		-evaluate goodness of new hand
        -if new score > old, return "discard" and index
        -return "get deck exchange"
        """
        
        observeOpponentMove(move)
        oldscore = evaluateRack(self.game.currentRack) 
        newHand = self.game.currentRack.copy()
        placement = placeCard(newHand,self.game.discard_pile.last())
        newHand[placement] = self.game.discard_pile[len(self.game.discard_pile)-1]
        newScore = evaluateRack(newHand)
        if newScore > oldScore: 
            return ('request_discard', placement)
        return ('request_deck',None)
        
        	
	def drawCard(self,card):
        """
        receives card value
        evaluates optimal card placement
        """
        response = placeCard(self.game.currentRack,card)
		return response
        
    def placeCard(self,rack,card):
        placement_scores = []
        for i in range(len(self.game.current_rack)-1):
            newHand = rack.copy()
            newHand[i] = self.game.discard_pile[len(self.game.discard_pile)-1]
            placement_scores.append( evaluateRack(newHand),i )
        return max(placement_scores)[1]
        
    def evaluateRack(self, currentHand):
        rack_scores = [0 for i in currentHand]
        for i in xrange(len(currentHand)):
            #evaluate heuristics here
            score = 0
            faceval = currentHand[i]+1
            #dist from ideal hash
            score -= faceval/4 - i
            if 80-faceval <= 20-i :
                score-=5
            elif faceval <= i :
                score-=5
            if i< len(currentHand)-1 and currentHand[i+1] == faceVal+1:
                score += 5
                rack_scores[i+1] +=5
            if i < len(currentHand)-1 and faceval > currentHand[i+1]:
               score-=3
               if i<1:
                upperDist = abs(currentHand[i+1]-faceval)
                lowerDist = abs(currentHand[i-1]-faceval)
                if upperDist<5 and upperDist>1 or lowerDist<5 and upperDist>1:
                    score -= 3
            rackscores[i]+=score
        rack_scores = [(len(rack_scores)-i)**2 for i in rack_scores]
        return sum(rack_scores)
    	
        """
		GENERATES THE NEXT MOVE
		//step 0 observe opponent's last move and update accordingly
		//step 1
		-evaluate the goodness of our hand
			-get raw goodness from global
			-update scores with our heuristics
		-pick out the weakest card to discard(pop on min priority)
		-update card values in global
		//step 2
		-calc goodness on incoming cards
			-raw goodness is weighted by their expected value
		-pick best card to replace discarded
			 -fuzzy cards weighted by probablity of draw
			 -discard pile cards weighted by probability of helping?
		-update global and player rack
		-return action
		"""
		
        
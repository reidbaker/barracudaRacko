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
        newHand.replace(placement,self.game.discard_pile.last)
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
        return 0
        
    def evaluateRack(self, currentHand):
        score=0.0
        return score
    	
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
		
        
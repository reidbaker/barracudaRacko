class siftAgent(object):
    def __init__(self,game_object):
        """
        constructor for a SiftAgent
        initializes all necessary data
        """
        self.game = game_object #initial game data 
		self.scored_ global_rack = [] #global rack with current value of all cards [list]
        self.scored_self_rack = [] #agent's own rack, ranked by expected value of cards in rack (min heap)
		self.fuzzy_rack = [] #rack of cards with unknown status, where current value is weighted by probability (max heap)
		
        
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
		return
		
	def drawCard(self):
		return
		
	
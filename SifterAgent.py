class SiftAgent(object):
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
    
	def recievePlayerMove(self,move):
        """
        observe the opponent move
        updates card all values
        """
        return
    
	def generateAction(self):
		"""
		GENERATES THE NEXT MOVE
		//step 1
		-evaluate the goodness of our hand
		-pick out the weakest card to discard(pop on min priority)
		-update all card values
		//step
		"""
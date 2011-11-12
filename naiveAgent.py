class naiveAgent(object):
    def __init__(self,game_object):
        """
        constructor for a naiveAgent
        initializes all necessary data
        """
        self.game = game_object
        
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
        """
        return {'move': 'request_deck'} # this is a super dummy move to make, remove when we have brains
    
    def drawCard(self,card):
        response = card/4
        # if rack[response]<card:
        # for i in range(0,len(range))
        if response>=20:
            response=19
        elif response<=-1:
            response = 0
        
        if response>=0 and response<=19:
            return response
        else:
            print "big fucking error: " + str(response)
            return 7